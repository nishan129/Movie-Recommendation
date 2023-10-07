from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifact
from src.constant.training_pipeline import filepath
from src.exception import ModelException
from src.ml.enstimator import preprocess,gerns,cast,crew,sem
import sys
import pandas as pd

class DataTransformation:
    
    def __init__(self,filepath:filepath,data_transformation_config:DataTransformationConfig):
        """
        This function is return recomandaiton object
        """
        try:
            self.filepath = filepath
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise ModelException(e,sys)
        
        
    @staticmethod
    def read_data(filepath)-> pd.DataFrame:
        try:
            creadit = filepath['credits']
            movie = filepath['movie']

            movie = preprocess(credit=creadit,movie=movie)
            return movie
        except Exception as e:
            raise ModelException(e,sys)
    
    def Clean_Data(movie):
        try:
            movie['genres'] = movie['genres'].apply(gerns)
            movie['cast']  = movie['cast'].apply(cast)
            movie['crew'] = movie['crew'].apply(crew)
            movie['overview'] = movie['overview'].apply(lambda x:x.split())
            movie['keywords'] =movie['keywords'].apply(cast)
            
            movie['tags'] = movie['overview'] + movie['genres'] + movie['keywords'] + movie['cast'] + movie['crew']
            movie['tags'] = movie['tags'].apply(lambda x:" ".join(x))
            movie['tags'] = movie['tags'].apply(lambda x:x.lower()) 
            
            movie = movie[['title','movie_id','tags']]
            
            movie['tags'] = movie['tags'].apply(sem)
            return movie
        except Exception as e:
            raise ModelException(e,sys)
        
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        
        data1 = DataTransformation.read_data(filepath=self.filepath)
        data = DataTransformation.Clean_Data(movie=data1)
        print(data.head())
        