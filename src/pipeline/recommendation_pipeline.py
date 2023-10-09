from src.entity.artifact_entity import DataTransformationArtifact
from src.logger import logging
from src.exception import ModelException
from src.utils.main_utils import load_object
import pandas as pd

class Movierecomandation:
    
    def __init__(self,data_transform_artifacat:DataTransformationArtifact):
        self.data_transform_artifact = data_transform_artifacat
    
    
    def recommend(movi):
    #movie = pd.read_csv()
    index = movie[movie['title'] == movi].index[0]
    distance = similarity[index]
    movie_list = sorted(list(enumerate(distance)), reverse=True,key=lambda x:x[1])[1:10]
    
    for i in movie_list:
        print(movie.iloc[i[0]].title)

