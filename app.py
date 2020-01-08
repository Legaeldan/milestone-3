import os
import random
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'drinks_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:passw0rd@myfirstcluster-ludvv.mongodb.net/drinks_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html', drinks=mongo.db.drinks.find())


@app.route('/discover')
def discover():
    rand = mongo.db.drinks.count()
    return render_template('viewdrink.html', drink=mongo.db.drinks.find()[random.randrange(rand)], ingredients=mongo.db.ingedients.find())

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', ingredients=mongo.db.ingedients.find())

@app.route('/add_ingredient')
def add_ingredient():
    return render_template('addingredient.html')

@app.route('/insert_ingredient', methods=['GET','POST'])
def insert_ingredient():
    ingredients =  mongo.db.ingedients
    ingredients.insert_one(request.form.to_dict())
    return redirect(url_for('ingredients'))

@app.route('/collection')
def collection():
    return render_template('collection.html', drinks=mongo.db.drinks.find())

@app.route('/view_drink/<drink_id>')
def view_drink(drink_id):
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('viewdrink.html', drink=the_drink, ingredients=mongo.db.ingedients.find())

@app.route('/add_drink')
def add_drink():
    return render_template('adddrink.html', ingredients=mongo.db.ingedients.find())

@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    drinks =  mongo.db.drinks
    return redirect(url_for('drink_ingredients', drink_id=drinks.insert_one(request.form.to_dict()).inserted_id))

@app.route('/drink_ingredients/<drink_id>', methods=['GET', 'POST'])
def drink_ingredients(drink_id):
    drink =  mongo.db.drinks
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('drinkingredients.html', drink=the_drink, drink_id=drink_id, ingredients=mongo.db.ingedients.find())

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

@app.route('/edit_drink/<drink_id>')
def edit_drink(drink_id):
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('editdrink.html', drink=the_drink, drink_id=drink_id)

@app.route('/edit_drink/update/<drink_id>', methods=['POST'])
def update_drink(drink_id):
    drink =  mongo.db.drinks
    drink.update_one( {'_id': ObjectId(drink_id)},
    { '$set':
        {
        'drinkImage':request.form.get('drinkImage'),
        'drinkName':request.form.get('drinkName')
        }    
    },
    upsert=False,)
    return redirect(url_for('view_drink', drink_id=drink_id))

@app.route('/search/<ingredient_id>')
def search_ingredient(ingredient_id):
    the_ingredient =  mongo.db.ingedients.find_one({"_id": ObjectId(ingredient_id)})
    return render_template('search_ingredient.html', ingredient=the_ingredient, drinks=mongo.db.drinks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(9100),
            debug=True)