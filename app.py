import os
import random
import datetime
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

APP.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

MONGO = PyMongo(APP)


@APP.route('/')
def home():
    """
    Renders homepage, and generates all drinks in db.

    Sorts in reverse order by key modifiedDate.
    """
    today = datetime.datetime.now()
    sorted_drinks = MONGO.db.drinks.find().sort('modifiedDate', -1)
    print(today)
    return render_template('home.html',
                           drinks=sorted_drinks,
                           headerTitle="Latest Drinks",
                           ingredients=MONGO.db.ingedients.find())


@APP.route('/logout')
def logout():
    """
    Checks if user is logged in. Prevents non-logged in users accessing logout function.

    If user is logged in, terminate session.

    If no user logged in, sent to home page.
    """
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('home'))


@APP.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form.to_dict()
        users = MONGO.db.users
        login_user = users.find_one({'username': form['username']})
        if login_user:
            if bcrypt.hashpw(form['password'].encode('utf-8'),
                             login_user['password']) == login_user['password']:
                session['username'] = form['username']
                return redirect(url_for('home'))
        return render_template('login.html', exists=0)
    return render_template('login.html')


@APP.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        form = request.form.to_dict()
        users = MONGO.db.users
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            print(existing_user)
            hashpass = bcrypt.hashpw(
                form['password'].encode('utf-8'), bcrypt.gensalt())
            user_details = {
                'username': form["username"],
                'email': form["email"],
                'password': hashpass
            }
            users.insert_one(user_details)
            session['username'] = form['username']
            return redirect(url_for('home'))
        return 'That username already exists!'
    return render_template('register.html')

@APP.route('/ingredients', methods=['GET', 'POST'], defaults={'ingredient_name': {}})
@APP.route('/ingredients/<ingredient_name>', methods=['GET', 'POST'])
def ingredients(ingredient_name):
    """
    Renders all ingredients within page.

    Retrieves all documents from ingredients database.
    """
    ingredients_list = MONGO.db.ingedients.find()
    drinks_list = MONGO.db.drinks.find()
    ingredient_dict = {
        'ingredientList': ingredient_name
    }
    print(ingredient_dict)
    if request.method == 'POST':
        ingredient_search = request.form.to_dict()
        print(ingredient_search)
        return render_template('ingredients.html', ingredients=ingredients_list,
                               ingredient=ingredient_search, drinks=drinks_list)
    return render_template('ingredients.html', drinks=drinks_list,
                           ingredient=ingredient_dict, ingredients=ingredients_list)


@APP.route('/collection/<collectionType>')
@APP.route('/collection/', defaults={'collectionType':{}})
def collection(collectionType):
    """
    Renders page which display all drinks in drinks database.
    """
    if collectionType == 'my-drinks':
        if 'username' in session:
            return render_template('mycollection.html', drinks=MONGO.db.drinks.find())
        return redirect(url_for('login'))
    return render_template('collection.html', drinks=MONGO.db.drinks.find())

@APP.route('/add-ingredient', methods=['POST', 'GET'])
def add_ingredient():
    """
    Renders standard add ingredient page.
    """
    if request.method == 'POST':
        ingredients_list = MONGO.db.ingedients
        today = datetime.datetime.now()
        form = request.form.to_dict()
        final_ingredient = {
            'ingredientName': form["ingredientName"].title(),
            'ingredientImage': form["ingredientImage"],
            'modifiedDate': str(today)
        }
        mongo_count = ingredients_list.find_one(
            {'ingredientName': form["ingredientName"]})
        if mongo_count is None:
            ingredients_list.insert_one(final_ingredient)
            return redirect(url_for('add_drink'))
        return render_template('addingredient.html', exists=1, ingredient=final_ingredient)
    return render_template('addingredient.html')


@APP.route('/view-drink/<drink_id>', methods=['POST', 'GET'])
def view_drink(drink_id):
    
    """
    Renders page for viewing all drink details for drink found in DB.
    """
    if request.method == 'POST':
        drinks = MONGO.db.drinks
        today = datetime.datetime.now()
        drinks.update_one({'_id': ObjectId(drink_id)},
                          {'$set':
                           {
                               'drinkImage': request.form.get('drinkImage'),
                               'drinkName': request.form.get('drinkName'),
                               'ingredientList': request.form.getlist("ingredientName"),
                               'modifiedDate': str(today),
                               'instructions': request.form.get('instructions')
                           }
                           },
                          upsert=False)
        return render_template('viewdrink.html',
                               drink=MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)}),
                               headerTitle=request.form.get('drinkName'),
                               ingredients=MONGO.db.ingedients.find())
    elif drink_id == 'randomDrink':
        rand = MONGO.db.drinks.count()
        the_drink = MONGO.db.drinks.find()[random.randrange(rand)]
        return render_template('viewdrink.html',
                               drink=the_drink,
                               headerTitle=the_drink['drinkName'],
                               ingredients=MONGO.db.ingedients.find())
    the_drink = MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)})
    print(the_drink)
    return render_template('viewdrink.html',
                           drink=the_drink,
                           headerTitle=the_drink['drinkName'],
                           ingredients=MONGO.db.ingedients.find())


@APP.route('/delete-drink/<drink_id>')
def delete_drink(drink_id):
    """
    Deletes drink from collection once confirmed on page.
    """
    MONGO.db.drinks.delete_one({"_id": ObjectId(drink_id)})
    return redirect(url_for('collection'))

@APP.route('/insert-drink', methods=['POST'])
def insert_drink():
    """
    Passthrough to push drink to DB.

    Creates a new object called final_drink
    then pulls all detauls from the form, including
    an array of ingredients.

    Finally, inserts new dictionary into DB.
    """
    drinks = MONGO.db.drinks
    form = request.form.to_dict()
    today = datetime.datetime.now()
    final_drink = {
        'drinkName': form["drinkName"].title(),
        'drinkImage': form["drinkImage"],
        'ingredientList': request.form.getlist("ingredientName"),
        'instructions': form["instructions"],
        'modifiedDate': str(today),
        'createdBy': session['username'],
    }
    return redirect(url_for('view_drink',
                            drink_id=drinks.insert_one(final_drink).inserted_id))

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
