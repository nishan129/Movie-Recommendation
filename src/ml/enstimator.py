from src.exception import ModelException
from src.logger import logging
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer 
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(credit,movie):
    logging.info("preprocessing is start")
    credit = pd.read_csv(credit)
    movie = pd.read_csv(movie)
    
    movie = movie[['genres','keywords','original_language','overview','title']]
    
    movie = movie.merge(credit,on='title')
    movie.dropna(inplace=True)
    
    movie =  movie[movie['original_language']== 'en']
    movie.drop('original_language',axis='columns',inplace=True)
    
    return movie

def gerns(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l

def cast(obj):
    l = []
    con = 0
    for i in ast.literal_eval(obj):
        if con != 3:
            l.append(i['name'])
            con += 1
        else: 
            break
    return l 

def crew(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            l.append(i['name'])
    return l

def sem(text):
    y = []
    pm = PorterStemmer()
    for i in text.split():
        y.append(pm.stem(i))
    return " ".join(y)