import os
import random
import datetime
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

#APP.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
APP.config["SECRET_KEY"] = "vRb81oq80xFpG45So4CKACqU1GvA9Fv"
APP.config["MONGO_DBNAME"] = "drinks_manager"
APP.config["MONGO_URI"] = "mongodb+srv://root:passw0rd@myfirstcluster-ludvv.mongodb.net/drinks_manager?retryWrites=true&w=majority"
#APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
#APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

MONGO = PyMongo(APP)


@APP.route('/')
def home():
    """
    Renders homepage, and generates all drinks in db
    """
    today = datetime.datetime.now()
    sortedDrinks = MONGO.db.drinks.find().sort('modifiedDate', -1)
    print(today)
    return render_template('home.html', drinks=sortedDrinks)

@APP.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('home'))

@APP.route('/login')
def login():
    return render_template('login.html')

@APP.route('/login-user', methods=['POST'])
def login_user():
    form = request.form.to_dict()
    print(form)
    users = MONGO.db.users
    login_user = users.find_one({'username' : form['username']})
    print(login_user)
    if login_user:
        if bcrypt.hashpw(form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = form['username']
            return redirect(url_for('home'))

    return render_template('login.html')

@APP.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        form = request.form.to_dict()
        users = MONGO.db.users
        existing_user = None
        if existing_user is None:
            hashpass = bcrypt.hashpw(form['password'].encode('utf-8'), bcrypt.gensalt())
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

@APP.route('/random')
def random_drink():
    """
    Count all document in drinks collection.
    return random document from drinks collection based on location of randomly generated number.
    Page with random document generation.
    """
    rand = MONGO.db.drinks.count()
    the_drink = MONGO.db.drinks.find()[random.randrange(rand)]
    return render_template('viewdrink.html', random=1,
                           drink=the_drink, ingredients=MONGO.db.ingedients.find())


@APP.route('/ingredients')
def ingredients_list():
    """
    Renders all ingredients within page.
    Retrieves all documents from ingredients database.
    """
    return render_template('ingredients.html', ingredients=MONGO.db.ingedients.find())

@APP.route('/search', methods=['POST'])
def search_ingredient():
    """
    Page to search for all documents containing an ingredient.
    Convert ingredient from ingredient page form into dictionary.
    """
    ingredient_search = request.form.to_dict()
    return render_template('search_ingredient.html',
                           ingredient=ingredient_search, drinks=MONGO.db.drinks.find())

@APP.route('/collection')
def collection():
    """
    Display all documents in collection in alphabetical order.
    """
    return render_template('collection.html', drinks=MONGO.db.drinks.find())

@APP.route('/add-ingredient', defaults={'ingredient_name': None})
@APP.route('/add-ingredient/<ingredient_name>')
def add_ingredient(ingredient_name):
    print(ingredient_name)
    """
    Renders standard add ingredient page.
    """
    
    return render_template('addingredient.html', ingredient=ingredient_name)

#@APP.route('/insert_ingredient', methods=['POST'])
#def insert_ingredient():
    #today = datetime.datetime.now()
    #form = request.form.to_dict()
    #finalIngredient = {
    #    'ingredientName': form["ingredientName"],
    #    'ingredientImage': form["ingredientImage"],
    #    'modifiedDate': (str(today.day)+"/"+str(today.month)+"/"+str(today.year))
    #}
    #MONGO.db.ingredients.insert_one(finalIngredient)
    #return redirect(url_for('add_drink'))

# Route when ingredients don't already exist.
#@APP.route('/add_ingredient/<drink_id>')
#def add_ingredient(drink_id):
    #the_drink = drink_id
    #return render_template('addingredient.html', drink_id=the_drink)
@APP.route('/insert-ingredient', methods=['POST'])
def insert_ingredient():
    """
    Passthrough page to insert new ingredient into DB.
    Pulls form, and converts to dictionary.
    Then redefines dictionary to add modified date into document.
    If check checks if document with same name already exists, then
    inserts if no ingredient already exists in db.
    """
    ingredients = MONGO.db.ingedients
    today = datetime.datetime.now()
    form = request.form.to_dict()
    finalIngredient = {
        'ingredientName': form["ingredientName"].title(),
        'ingredientImage': form["ingredientImage"],
        'modifiedDate': str(today)
    }
    mongo_count = ingredients.find_one({'ingredientName': form["ingredientName"]})
    if mongo_count is None:
        print("Inserting ingredient")
        print(mongo_count)
        ingredients.insert_one(finalIngredient)
        return redirect(url_for('add_drink'))
    print("Ingredient already exists. Returning to page.")
    return redirect(url_for('add_ingredient', ingredient_name=form["ingredientName"]))

@APP.route('/view-drink/<drink_id>')
def view_drink(drink_id):
    """
    Route to view all drink details including ingredients and image
    """
    the_drink = MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('viewdrink.html', drink=the_drink)

@APP.route('/delete-drink/<drink_id>')
def delete_drink(drink_id):
    """
    Deleted drink from collection once confirmed on page.
    """
    MONGO.db.drinks.delete_one({"_id": ObjectId(drink_id)})
    return redirect(url_for('collection'))


@APP.route('/add-drink')
def add_drink():
    """
    Renders add drink page.
    Populates ingredient list to add to ingredient list array within drink.
    """
    return render_template('adddrink.html', ingredients=MONGO.db.ingedients.find())

@APP.route('/insert-drink', methods=['POST'])
def insert_drink():
    """
    Passthrough to push drink to DB.
    """
    drinks = MONGO.db.drinks
    form = request.form.to_dict()
    today = datetime.datetime.now()
    finalDrink = {
        'drinkName': form["drinkName"].title(),
        'drinkImage': form["drinkImage"],
        'ingredientList': request.form.getlist("ingredientName"),
        'instructions': form["instructions"],
        'modifiedDate': str(today)
    }
    return redirect(url_for('view_drink', drink_id=drinks.insert_one(finalDrink).inserted_id))


#@APP.route('/drink_ingredients/<drink_id>', methods=['GET', 'POST'])
#def drink_ingredients(drink_id):
    #drink = MONGO.db.drinks
    # drink_id pulled from previous to add ingredients to newly created object.
    #the_drink = MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)})
    #return render_template('drinkingredients.html', drink=the_drink, drink_id=drink_id, ingredients=MONGO.db.ingedients.find())

# Passthrough page to insert ingredients array into document created previously, or to edit current drink.
# Insert split from initial drink creation to facilitate the creation of an array in MongoDB.
#@APP.route('/drink_ingredients/insert/<drink_id>', methods=['POST'])
#def insert_ingredients(drink_id):
    #drink = MONGO.db.drinks
    #drink.update_one({'_id': ObjectId(drink_id)},
    #                 {'$set':
    #                  {
    #                      'ingredientList': request.form.getlist('ingredientName')
    #                  }
    #                  })
    #return redirect(url_for('view_drink', drink_id=drink_id))

@APP.route('/edit-drink/<drink_id>')
def edit_drink(drink_id):
    """
    Find drink details, and generate on page for editing purposes.
    """
    ingredientList = MONGO.db.ingedients.find()
    the_drink = MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('editdrink.html',
                           ingredients=ingredientList, drink=the_drink, drink_id=drink_id)

@APP.route('/edit-drink/update/<drink_id>', methods=['POST'])
def update_drink(drink_id):
    """
    Update drink passthrough page to push to DB.
    Update only set object in document, not all using $set function.
    upsert set to False to avoid creating new document. Only update existing.

    """
    drink = MONGO.db.drinks
    today = datetime.datetime.now()
    drink.update_one({'_id': ObjectId(drink_id)},
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
    return redirect(url_for('view_drink', drink_id=drink_id))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(9100),
            debug=True)
