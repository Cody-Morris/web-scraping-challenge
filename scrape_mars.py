from bs4 import BeautifulSoup as bs
import os
import requests
import pymongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit('https://redplanetscience.com/')
html = browser.html


soup = bs(html, 'html.parser')
# Retrieve all elements that contain book information
titles = soup.find_all('div', class_='content_title')

cleantitles = []

for title in titles:
    # print (title.text)
    cleantitles.append(title.text)

print(cleantitles) 


# %%
paras = soup.find_all('div', class_='article_teaser_body')

cleanparas = []

for para in paras:
    # print (title.text)
    cleanparas.append(para.text)

print(cleanparas) 


# %%
browser.visit('https://spaceimages-mars.com/')
html = browser.html

soup = bs(html, 'html.parser')
    # Retrieve all elements that contain book information
pics = soup.find_all('img', class_='thumbimg')

cleanpics = []

for pic in pics:
    # print (title.text)
    cleanpics.append(pic['src'])

print(cleanpics) 


# %%
df = pd.read_html('https://galaxyfacts-mars.com/') 
df[0]
# df[1]


# %%
cleanoriginaltitles = []
cleanoriginalpics = []

for counter in range(4):
    browser.visit('https://marshemispheres.com/')
    browser.find_by_css('a.product-item img')[counter].click()
    html = browser.html
    soup = bs(html, 'html.parser')
    # Retrieve all elements that contain book information
    originalpics = soup.find_all('a', text='Original')
    originaltitles = soup.find_all('h2', class_='title')
    
    for originalpic in originalpics:
        cleanoriginalpics.append(originalpic['href'])

    for originaltitle in originaltitles:
        cleanoriginaltitles.append(originaltitle.text)
    
print(cleanoriginalpics)
print(cleanoriginaltitles) 


# %%
hemisphere_image_urls = []

for counter in range(4):
    hemisphere_image_urls.append({'Titles': cleanoriginaltitles[counter],'img_url': cleanoriginalpics[counter]})

print(hemisphere_image_urls)


# %%
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

for counter in range(4):
    db = client.Mars_db
    collection = db.items
    collection.insert_one(hemisphere_image_urls[counter])



listings = db.items.find()

for listing in listings:
    print(listing)