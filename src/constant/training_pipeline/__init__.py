import os

# defining common constants variable for training pipeline
PIPELINE_NAME: str = "movie"
ARTIFACT_DIR: str = "artifact"

PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

# Datafile path 

filepath = {"credits":"D:/Machine Learning project/Movie-Recommendation/Movie-Recommendation/artifact/Dataset/tmdb_5000_credits.csv",
            "movie":"D:/Machine Learning project/Movie-Recommendation/Movie-Recommendation/artifact/Dataset/tmdb_5000_movies.csv"}

# Data Transformation dir name

DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

