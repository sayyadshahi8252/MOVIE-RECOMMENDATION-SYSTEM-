# -*- coding: utf-8 -*-
"""MOVIE RECOMMENDATION SYSTEM .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cynosrd7TnhKoQMg_AjRd4FUu2E8B2d8

***TITLE OF PROJECT:***

### MOVIE RECOMMENDATION SYSTEM

### **Objective**
A recommender system is a tool that helps predict or filter preferences based on a user’s past choices. These systems are used widely across different areas like movies, music, news, books, research articles, search queries, social tags, and products.

There are two main ways a recommender system can suggest items:

**Collaborative Filtering:** This approach creates a model based on a user's past behavior, such as items they bought or searched for, and finds similar behaviors from other users. The model then predicts items (or ratings for items) that the user might like based on shared interests with others.

**Content-Based Filtering:** This approach uses specific features of an item to recommend other similar items. It relies completely on descriptions of the items and a profile of the user’s preferences. The system suggests items that are similar to what the user has liked in the past.

Let’s build a basic recommendation system using Python and Pandas. This system will suggest items that are most similar to a particular item—in this case, movies. It will show which movies are most similar to the user’s choice.

### **Import Library**
"""

import pandas as pd

import numpy as np

"""### **Import Data**"""

data = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Movies%20Recommendation.csv')

"""### **Describe Data**"""

data.head()

data.describe()

data.info()

data.columns

"""### **Data Preprocessing**"""

data.isna().sum()

"""### **Define Target Variable (y) and Feature Variables (X)**"""

data_features = data[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')
data_features.shape

data_features

X = data_features['Movie_Genre'] +' '+ data_features['Movie_Tagline'] +' '+ data_features['Movie_Keywords'] +' '+ data_features['Movie_Director'] +' '+ data_features['Movie_Cast']
X.shape

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()

X = tfidf.fit_transform(X)

X.shape

print(X)

"""### **Modeling**"""

from sklearn.metrics.pairwise import cosine_similarity

similarity_score = cosine_similarity(X)
similarity_score

similarity_score.shape

"""### **Prediction**"""

movie = input("enter title of your favourite movie: ")

movie_titles_list = data['Movie_Title'].tolist()

import difflib

movie_recommendation = difflib.get_close_matches(movie, movie_titles_list)
print(movie_recommendation)

close_match = movie_recommendation[0]
index_close_match = data[data.Movie_Title == close_match]['Movie_ID'].values[0]

rec_score = list(enumerate(similarity_score[index_close_match]))
print(rec_score)

sorted_similar_movies = sorted(rec_score, key = lambda x: x[1], reverse = True)

n = int(input("enter no of movies to suggest: "))

print("top",n,"recommended movies for you: ")
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = data[data.Movie_ID == index]['Movie_Title'].values
  if i < n+1:
    print(i,")",title_from_index)
    i+=1

