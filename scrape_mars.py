import re
from bs4 import BeautifulSoup as bs
import os
import requests
import pymongo
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser



def scrape():
    # data = {}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit('https://redplanetscience.com/')
    # time.sleep(2)
    html = browser.html
    # browser = Browser('chrome', **executable_path, headless=False)
    # title, parapraph = news(browser)
    



    # return data


# def news(browser):
    # browser.visit('https://redplanetscience.com/')
    # title = browser.find_by_css('div.content_title').text
    # paragraph = browser.find_by_css('div.article_teaser_body').text
    # return title, paragraph



    soup = bs(html, 'html.parser')
    # time.sleep(3)
    # Retrieve all elements that contain book information
    titles = soup.find('div', class_="content_title")
    print(f'************************************************************************************************{titles}')

    cleantitles = []

    # for title in titles:
        # print (title.text)
    cleantitles.append(titles.text)

    print(cleantitles) 


    # %%
    paras = soup.find('div', class_='article_teaser_body')

    cleanparas = []

    # for para in paras:
        # print (title.text)
    cleanparas.append(paras.text)

    print(cleanparas) 


    # %%
    browser.visit('https://spaceimages-mars.com/')
    # time.sleep(2)
    html = browser.html

    soup = bs(html, 'html.parser')
    # time.sleep(3)
        # Retrieve all elements that contain book information
    pics = soup.find('img', class_='thumbimg')

    cleanpics = []

    # for pic in pics:
        # print (title.text)
    cleanpics.append(pics['src'])

    print(cleanpics) 


    # %%
    df = pd.read_html('https://galaxyfacts-mars.com/')[0].to_html() 
    # df[1]
    df= df.replace('\n','')


    # %%
    cleanoriginaltitles = []
    cleanoriginalpics = []

    for counter in range(4):
        browser.visit('https://marshemispheres.com/')
        browser.find_by_css('a.product-item img')[counter].click()
        # time.sleep(2)
        html = browser.html
        soup = bs(html, 'html.parser')
        # time.sleep(3)
        # Retrieve all elements that contain book information
        originalpics = soup.find('a', text='Original')
        originaltitles = soup.find('h2', class_='title')
        
        # for originalpic in originalpics:
        cleanoriginalpics.append(originalpics['href'])

        # for originaltitle in originaltitles:
        cleanoriginaltitles.append(originaltitles.text)
        
    print(cleanoriginalpics)
    print(cleanoriginaltitles) 


    # %%
    hemisphere_image_urls = []

    for counter in range(4):
        hemisphere_image_urls.append({'Titles': cleanoriginaltitles[counter],'img_url': cleanoriginalpics[counter]})

    print(hemisphere_image_urls)

    data = {
        'Titles': cleanoriginaltitles,
        'paragraph': cleanparas,
        'img_url' : cleanoriginalpics,
        'table' : df
    }
    return (data)
