from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
from bs4 import BeautifulSoup as bs
import os
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.Mars_db

# listings = db.items.find()

# for listing in listings:
#     print(listing)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    listings = db.items.find_one()
    # print(listings)
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scraper():
    # listings = mongo.db.listings
    listings = db.items.find_one()
    title = scrape_mars.cleantitles
    print(title)
    listings.update({}, title, upsert=True)
    return render_template("Clean.html", title=title, listings=listings)

    



if __name__ == "__main__":
    app.run(debug=True)