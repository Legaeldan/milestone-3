import os
import random
import datetime
from flask import Flask, render_template, redirect, request, url_for
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
    Renders homepage, and generates all drinks in db
    """
    return render_template('home.html', drinks=MONGO.db.drinks.find())

@APP.route('/discover')
def discover():
    """
    Count all document in drinks collection.
    return random document from drinks collection based on location of randomly generated number.
    Page with random document generation.
    """
    rand = MONGO.db.drinks.count()
    the_drink = MONGO.db.drinks.find()[random.randrange(rand)]
    return render_template('viewdrink.html', drink=the_drink, ingredients=MONGO.db.ingedients.find())


@APP.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', ingredients=MONGO.db.ingedients.find())

@APP.route('/search', methods=['POST'])
def search_ingredient():
    """
    Page to search for all documents containing an ingredient.
    Convert ingredient from ingredient page form into dictionary.
    """
    ingredient_search = request.form.to_dict()
    return render_template('search_ingredient.html', ingredient=ingredient_search, drinks=MONGO.db.drinks.find())

@APP.route('/collection')
def collection():
    """
    Display all documents in collection in alphabetical order.
    """
    return render_template('collection.html', drinks=MONGO.db.drinks.find())

@APP.route('/add_ingredient')
def add_ingredient():
    return render_template('addingredient.html')

@APP.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    form = request.form.to_dict()
    mongo_count = MONGO.db.ingredients.count_documents({'ingredientName': form["ingredientName"]})
    if mongo_count > 0:
        print(mongo_count)
        print(form)
    else:
        print(mongo_count)
        print(form)
        MONGO.db.ingredients.insert_one(form)
    return redirect(url_for('add_drink'))

# Route when ingredients don't already exist.
#@APP.route('/add_ingredient/<drink_id>')
#def add_ingredient(drink_id):
    #the_drink = drink_id
    #return render_template('addingredient.html', drink_id=the_drink)

# Passthrough page to insert new ingredient into DB.
#@APP.route('/insert_ingredient/<drink_id>', methods=['GET', 'POST'])
#def insert_ingredient(drink_id):
    #ingredients = MONGO.db.ingedients
    # drink_id defined to retain and pass to return back to drink being edited.
    #drink_id
    #ingredients.insert_one(request.form.to_dict())
    #return redirect(url_for('drink_ingredients', drink_id=drink_id))

@APP.route('/view_drink/<drink_id>')
def view_drink(drink_id):
    """
    Route to view all drink details including ingredients and image
    """
    the_drink = MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('viewdrink.html', drink=the_drink)

@APP.route('/delete_drink/<drink_id>')
def delete_drink(drink_id):
    """
    Deleted drink from collection once confirmed on page.
    """
    MONGO.db.drinks.delete_one({"_id": ObjectId(drink_id)})
    return redirect(url_for('collection'))


@APP.route('/add_drink')
def add_drink():
    return render_template('adddrink.html', ingredients=MONGO.db.ingedients.find())

@APP.route('/insert_drink', methods=['POST'])
def insert_drink():
    """
    Passthrough to push drink to DB.
    """
    drinks = MONGO.db.drinks
    form = request.form.to_dict()
    today = datetime.datetime.now()
    finalDrink = {
        'drinkName': form["drinkName"],
        'drinkImage': form["drinkImage"],
        'ingredientList': request.form.getlist("ingredientName"),
        'modifiedDate': (str(today.day)+"/"+str(today.month)+"/"+str(today.year))
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

@APP.route('/edit_drink/<drink_id>')
def edit_drink(drink_id):
    """
    Find drink details, and generate on page for editing purposes.
    """
    the_drink = MONGO.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('editdrink.html', drink=the_drink, drink_id=drink_id)

@APP.route('/edit_drink/update/<drink_id>', methods=['POST'])
def update_drink(drink_id):
    """
    Update drink passthrough page to push to DB.
    Update only set object in document, not all using $set function.
    upsert set to False to avoid creating new document. Only update existing.

    """
    drink = MONGO.db.drinks
    drink.update_one({'_id': ObjectId(drink_id)},
                     {'$set':
                      {
                          'drinkImage': request.form.get('drinkImage'),
                          'drinkName': request.form.get('drinkName')
                      }
                      },
                     upsert=False)
    return redirect(url_for('view_drink', drink_id=drink_id))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
