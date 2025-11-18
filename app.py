import streamlit as st
import pickle
import requests

# ------------------------------
# Fonction pour récupérer l'affiche du film (TMDB API)
# ------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# ------------------------------
# Chargement des données
# ------------------------------
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# ------------------------------
# Header principal
# ------------------------------
st.markdown("""
    <h1 style='text-align:center; font-size:2.5rem; font-weight:800; color:#ff4b4b;'>
        🎬 Movie Recommender System
    </h1>
""", unsafe_allow_html=True)

# ------------------------------
# Import du composant carousel
# ------------------------------
import streamlit.components.v1 as components
imageCarouselComponent = components.declare_component(
    "image-carousel-component", 
    path="frontend/public"
)

# ------------------------------
# Images des films populaires
# ------------------------------
imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]

# ------------------------------
# 🔥 Titre "Popular Movies"
# ------------------------------
st.markdown("""
    <div style='text-align:center; font-size:1.8rem; font-weight:700; margin-top:25px; margin-bottom:10px; color:#333;'>
        🔥 Popular Movies
    </div>
""", unsafe_allow_html=True)

# Carousel
imageCarouselComponent(imageUrls=imageUrls, height=200)

# ------------------------------
# Sélecteur de films
# ------------------------------
selectvalue = st.selectbox("Select a movie to get recommendations:", movies_list)

# ------------------------------
# Fonction de recommandation
# ------------------------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommend_movie = []
    recommend_poster = []

    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))

    return recommend_movie, recommend_poster

# ------------------------------
# Bouton + affichage des résultats
# ------------------------------
if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selectvalue)

    st.markdown("""
        <div style='text-align:center; font-size:1.6rem; font-weight:700; margin-top:25px; margin-bottom:20px; color:#4b4bff;'>
            🎯 Recommended Movies for You
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(movie_poster[0], use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:600;'>{movie_name[0]}</p>", unsafe_allow_html=True)

    with col2:
        st.image(movie_poster[1], use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:600;'>{movie_name[1]}</p>", unsafe_allow_html=True)

    with col3:
        st.image(movie_poster[2], use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:600;'>{movie_name[2]}</p>", unsafe_allow_html=True)

    with col4:
        st.image(movie_poster[3], use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:600;'>{movie_name[3]}</p>", unsafe_allow_html=True)

    with col5:
        st.image(movie_poster[4], use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-weight:600;'>{movie_name[4]}</p>", unsafe_allow_html=True)
