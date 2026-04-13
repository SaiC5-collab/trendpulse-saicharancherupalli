import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import matplotlib.lines as mlines

# Creating Master path for output folder
outputfolderpath = Path(f"{Path(__file__).resolve().parent.parent}\outputs")
outputfolderpath.mkdir(exist_ok=True)

#Load Trend Analysis data into dataframe

filepathAnalysis = f'{Path(__file__).resolve().parent.parent}\data\\trends_analysed.csv'
df = pd.read_csv(filepathAnalysis)

# Creating Horizontal barchat with Top 10 stories by Score

df_top10 = df.sort_values(by="score", ascending=False).head(10)
labels = [label[:50] for label in df_top10["title"]]
plt.barh(labels, df_top10['score'])
plt.title("Top 10 Stories by Score")
plt.xlabel("Scores")
plt.ylabel("Story Name")
plt.tight_layout()
plt.savefig(f"{outputfolderpath}\chart1_top_stories.png")
plt.show()

#Creating Bar Chart with Stories per Category

category_counts = df.groupby("category").size()
category_counts = category_counts.sort_values(ascending=False)
plt.figure(figsize=(8, 6))
plt.bar(category_counts.index, category_counts.values, color = ["green", "blue", "Yellow", "purple", "red"])
plt.title("Stories Per Category")
plt.xlabel("Category")
plt.ylabel("No of Stories")
plt.tight_layout()
plt.savefig(f"{outputfolderpath}\chart2_categories.png")
plt.show()

#Create Scatter plot between Score and Comments

plt.scatter(df['score'], df['num_comments'], c = ['red' if val == False else 'green' for val in df['is_popular'] ])
red_dot = mlines.Line2D([], [], color='red', marker='o' ,linestyle='None',label='Not Popular') # Defining Legend as per color 
green_dot = mlines.Line2D([], [], color='green',marker='o' , linestyle='None',label='Popular')
plt.title("Score vs Comments")
plt.legend(handles=[red_dot, green_dot])
plt.xlabel("Score")
plt.ylabel("No of Comments")
plt.tight_layout()
plt.savefig(f"{outputfolderpath}\chart3_scatter.png")
plt.show()
