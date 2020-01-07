import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'drinks_manager'
app.config["MONGO_URI"] = 'mongodb+srv://testuser:testuserpassw0rd@myfirstcluster-ludvv.mongodb.net/drinks_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', ingredients=mongo.db.ingedients.find())

@app.route('/collection')
def collection():
    return render_template('collection.html', drinks=mongo.db.drinks.find())

@app.route('/view_drink/<drink_id>')
def view_drink(drink_id):
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('viewdrink.html', drink=the_drink, ingredients=mongo.db.ingedients.find())

@app.route('/edit_drink/<drink_id>')
def edit_drink(drink_id):
    the_drink =  mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template('editdrink.html', drink=the_drink)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(9100),
            debug=True)