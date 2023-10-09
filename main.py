from src.constant.training_pipeline import ARTIFACT_DIR
from src.components.data_transformation import DataTransformation
from src.constant.training_pipeline import filepath
from src.entity.config_entity import DataTransformationConfig
from src.pipeline.trainingpipeline import TraningPipeline
import streamlit as st
import pandas as pd
import pickle
import requests

trainig = TraningPipeline()
artifact = trainig.run_pipeline()
    


def poster_fatch(movie_id):
    
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recomend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(poster_fatch(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


movie_list = pickle.load(open(artifact.transformed_data_file_path,'rb'))
movies = pd.DataFrame(movie_list)
similarity = pickle.load(open(artifact.transformed_object_file_path,'rb'))

st.title('Movie Recomdation System')


option = st.selectbox('Select Movie',movies['title'].values)

if st.button('Search Movie'):
    names, poster = recomend(option)
    
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    
    with col1:
        st.text(names[0])
        st.image(poster[0])
        
    with col2:
        st.text(names[1])
        st.image(poster[1])
        
    with col3:
        st.text(names[2])
        st.image(poster[2])
        
    with col4:
        st.text(names[3])
        st.image(poster[3])
        
    with col5:
        st.text(names[4])
        st.image(poster[4])
        
        