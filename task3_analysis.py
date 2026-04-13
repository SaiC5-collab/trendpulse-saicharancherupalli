import pandas as pd
import json
from datetime import datetime
import time
from pathlib import Path
import numpy as np

#Load Imported data from Hacker news into Dataframe

trendsfile= f'{Path(__file__).resolve().parent.parent}\data\\trends_clean.csv'

df = pd.read_csv(trendsfile)
df = df[df['category'] != "No Match"]
#Display First Five Rows
print(df.head(5))

#Display Shape of Trends Table
print(df.shape)

#Display Average Scores and Average Comments per story
print(f"Average Score Per Story: {df['score'].mean()}")
print(f"Average Comments Per Story: {df['num_comments'].mean()}")

# Calculating Mean, Median and standard deviation of Column "Score"
score_mean = np.mean(np.array(df['score']))
score_median = np.median(np.array(df['score']))
score_std = np.std(np.array(df['score']))
max_score = np.max(df['score'])
min_score = np.min(df['score'])


print(f"Mean of field Score is {score_mean}, Median is {score_median} and Standard deviation is {score_std}")
print(f"Maximum score per story that acheived is : {max_score}")
print(f"Minimum score per story that acheived is : {min_score}")

# Calculating the most no of stories per cateory

top_category = df['category'].value_counts().idxmax()
maxstorypercategory = df['category'].value_counts().max()

print(f" Category: {top_category} has most stories ({maxstorypercategory})")

# Calculating which story has more no of comments

maxnoof_comments = df['num_comments'].max()
storywithmostcomments = df.loc[df['num_comments'] == maxnoof_comments, 'title']

print(f"Story: {storywithmostcomments.iloc[0]} has received most number of comments i.e.., {maxnoof_comments}")

# Adding 2 new columns i.e.., engaement and is_popular

df['engaged'] = df['num_comments']/(df['score']+1) 
df['is_popular'] = np.where(df['score'] > score_mean, True, False)

df.to_csv("data\\trends_analysed.csv")

print("data saved into trends_analysed file in data folder.")