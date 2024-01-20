import streamlit as st 
import pandas as pd
#import pickle
st.header("Movie Recommender System") 

movies = pd.read_pickle(open('movies_list.pkl', 'rb'))
similarity = pd.read_pickle(open('similarity.pkl', 'rb'))

movies_list = movies["title"].values
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
  index = movies[movies['title']==movie].index[0]
  distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])[1:6]
  recommend_movie=[]
  
  for i in distance:
    recommend_movie.append(movies.iloc[i[0]].title)
  return recommend_movie

if st.button("Show Reccomendation"):
  movie_name = recommend(selectvalue)
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.text(movie_name[0])
  with col2:
    st.text(movie_name[1])
  with col3:
    st.text(movie_name[2])
  with col4:
    st.text(movie_name[3])
  with col5:
    st.text(movie_name[4])        