def scrape():

    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup
    import requests
    import pymongo
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, inspect, func
    import json
    import warnings
    
    news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
    news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

    # Current Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets = soup.find_all("p",{"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    mars_weather = tweets[0].text
    print(mars_weather)

    # Mars Facts
    col1 = []
    col2 = []
    url = 'https://space-facts.com/mars/'
    response = requests.get(url)
    soup_mf = BeautifulSoup(response.text, 'html.parser')
    mf1 = soup_mf.find_all("td",{"class": "column-1"})
    for item in mf1:
        col1.append(item.find_all("strong")[0].text)
            
    mf2 = soup_mf.find_all("td",{"class": "column-2"})
    for item2 in mf2:
        col2.append(item2.get_text())   
    mars_facts = list(zip(col1, col2))
        
    # Hemisphere pictures 
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        ]

    return render_template("mars_index.html", news_title = news_title, news_p = news_p, mars_weather = mars_weather, mars_facts = mars_facts, hemisphere_image_urls = hemisphere_image_urls )