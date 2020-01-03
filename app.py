import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'drinks_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

@app.route('/collection')
def collection():
    return render_template('collection.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(9100),
            debug=True)