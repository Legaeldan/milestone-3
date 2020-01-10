import os
import random
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'drinks_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html', drinks=mongo.db.drinks.find())

#Page with random document generation.
@app.route('/discover')
def discover():
    #Count all document in drinks collection.
    rand = mongo.db.drinks.count()
    #return random document from drinks collection based on location of randomly generated number.
    the_drink = mongo.db.drinks.find()[random.randrange(rand)]
    return render_template('viewdrink.html', drink=the_drink, ingredients=mongo.db.ingedients.find())

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', ingredients=mongo.db.ingedients.find())

#Page to search for all documents containing an ingredient.
@app.route('/search', methods=['POST'])
def search_ingredient():
    #Convert ingredient from ingredient page form into dictionary.
    ingredients = request.form.to_dict()
    return render_template('search_ingredient.html', ingredient=ingredients, drinks=mongo.db.drinks.find())

#Display all documents in collection in alphabetical order.
@app.route('/collection')
def collection():
    return render_template('collection.html', drinks=mongo.db.drinks.find())

#Route when ingredients don't already exist.
@app.route('/add_ingredient/<drink_id>')
def add_ingredient(drink_id):
    the_drink = drink_id
    return render_template('addingredient.html', drink_id=the_drink)

#Passthrough page to insert new ingredient into DB.
@app.route('/insert_ingredient/<drink_id>', methods=['GET','POST'])
def insert_ingredient(drink_id):
    ingredients =  mongo.db.ingedients
    #drink_id defined to retain and pass to return back to drink being edited.
    drink_id
    ingredients.insert_one(request.form.to_dict())
    return redirect(url_for('drink_ingredients', drink_id=drink_id))

#View individual drink details.
@app.route('/view_drink/<drink_id>')
def view_drink(drink_id):
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('viewdrink.html', drink=the_drink, ingredients=mongo.db.ingedients.find())

#Deleted drink from collection once confirmed on page.
@app.route('/delete_drink/<drink_id>')
def delete_drink(drink_id):
    the_drink = mongo.db.drinks.delete_one({"_id": ObjectId(drink_id)})
    return redirect(url_for('collection'))

@app.route('/add_drink')
def add_drink():
    return render_template('adddrink.html', ingredients=mongo.db.ingedients.find())

#Passthrough to push drink to DB.
@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    drinks =  mongo.db.drinks
    #Inserted_id used to return _id for newly created document, and pass to next page.
    return redirect(url_for('drink_ingredients', drink_id=drinks.insert_one(request.form.to_dict()).inserted_id))

@app.route('/drink_ingredients/<drink_id>', methods=['GET', 'POST'])
def drink_ingredients(drink_id):
    drink =  mongo.db.drinks
    #drink_id pulled from previous to add ingredients to newly created object.
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('drinkingredients.html', drink=the_drink, drink_id=drink_id, ingredients=mongo.db.ingedients.find())

#Passthrough page to insert ingredients array into document created previously, or to edit current drink.
#Insert split from initial drink creation to facilitate the creation of an array in MongoDB.
@app.route('/drink_ingredients/insert/<drink_id>', methods=['POST'])
def insert_ingredients(drink_id):
    drink =  mongo.db.drinks
    drink.update_one( {'_id': ObjectId(drink_id)},
    { '$set':
        {
        'ingredientList':request.form.getlist('ingredientName')
        }       
    })
    return redirect(url_for('view_drink', drink_id=drink_id))

#Find drink details, and generate on page for editing purposes.
@app.route('/edit_drink/<drink_id>')
def edit_drink(drink_id):
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('editdrink.html', drink=the_drink, drink_id=drink_id)

#Update drink passthrough page to push to DB.
@app.route('/edit_drink/update/<drink_id>', methods=['POST'])
def update_drink(drink_id):
    drink =  mongo.db.drinks
    #Update only set object in document, not all
    drink.update_one( {'_id': ObjectId(drink_id)},
    #Function from Mongo to only update specified keys without overwriting document.
    { '$set':
        {
        'drinkImage':request.form.get('drinkImage'),
        'drinkName':request.form.get('drinkName')
        }    
    },
    #Upsert False to avoid creating new document. Only update existing documents.
    upsert=False)
    return redirect(url_for('view_drink', drink_id=drink_id))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)