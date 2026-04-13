
import pandas as pd
import json
from datetime import datetime
import time
import pathlib

#Load Imported data from Hacker news into Dataframe

fileJson= "D:\\Sai\\AI and ML\\Mini Project - 1\\data\\trends_20260413.json"

df = pd.read_json(fileJson)

print(f"Loaded {len(df)} rows from file: {fileJson}")

#Drop Duplicates from Column "post_id"

df = df.drop_duplicates(subset="post_id")

print(f"After Removing Duplicates: {len(df)}")

#Remove null values from column "Post_Id", "Title", "Score"

df= df[(df["post_id"] !=  "") | (df["title"] != "") | (df["score"] != "")]

print(f"After Removing Null Values: {len(df)}")

df["num_comments"]= df["num_comments"].astype(str).replace("Not Found",0).astype(int) #Converting datatype of column "num_comments" into Integer

# Remove rows where score is less than 5

df = df[df["score"] >= 5]

print(f"Rows: {len(df)} available after removing rows where score is less than 5")

df['title'] = df['title'].astype(str).str.strip()

print(df.info())

df.to_csv("data\\trends_clean.csv") # Saving Cleaned data into CSV file

print(df.groupby("category")['title'].count())


