import requests as req
import json
from datetime import datetime
import time
import pandas as pd
from pathlib import Path

#Define Category items
categorylist = {
    'technology' : ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    'worldnews' : ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    'sports' : ["NFL"," NBA"," FIFA"," sport"," game"," team"," player"," league"," championship"],
    'science' : ["research"," study"," space"," physics"," biology"," discovery"," NASA"," genome"],
    'entertainment' : ["movie"," film"," music"," Netflix"," game"," book"," show"," award"," streaming"]
}

#Collect Story ID's

try:

    url_topstories = "https://hacker-news.firebaseio.com/v0/topstories.json"

    headers = {"User-Agent": "TrendPulse/1.0"}

    response = req.get(url_topstories, headers=headers)

    storyids = response.json()
except SystemError as e:
    print(F"Api failed while collecting ID's: {e}")

#Define Function to decide the Category using keywords

def get_category(text, categories):
    text = text.lower()

    for category, keywords in categories.items():
        if any(keyword.lower() in text for keyword in keywords):
            return category

    return "No Match"

post_id = []
title = []
category = []
score = []
num_comments = []
author = []
collected_at = []


#Collect Stories by ID's extracted and store them in a DataFrame.

for id in storyids:

    try:
        url_storydetails = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        response= req.get(url_storydetails, headers=headers)
        if(response.status_code == 200):
            data = response.json()
            storycategory = data.get("title", "Not Found")

            # Define Category
            if(storycategory == "Not Found"):
                category.append("Category Not Found")
            else:
                storycategory = get_category(storycategory, categorylist)
                category.append(storycategory)

            post_id.append(data.get("id","Not Found"))
            title.append(data.get("title", "Not Found"))
            score.append(data.get("score", "Not Found"))
            num_comments.append(data.get("descendants","Not Found"))
            author.append(data.get("by","Not Found"))
            collected_at.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(2)

    except req.exceptions.ConnectionError:
        print("Network problem")

    except req.exceptions.Timeout:
        print("Request timed out")

    except req.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except ValueError:
        print("Invalid JSON response")
    except Exception as e:
        print("Something went wrong:", e) 

#Converting to DataFrame

df = pd.DataFrame({
    "post_id" : post_id,
    "title" : title,
    "category" : category,
    "score" : score,
    "num_comments" : num_comments,
    "author" : author,
    "collected_at" : collected_at
})

#Saving Collected story details to JSON file.

fileJson =  f'{Path.cwd()}\data\\trends_{datetime.now().strftime("%Y%m%d")}.json'
df.to_json(fileJson)

print(f"Collected {len(df)} stories and saved to file: {fileJson}")
    
