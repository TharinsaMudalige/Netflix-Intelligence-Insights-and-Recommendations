import streamlit as st
import pandas as pd
import joblib

# CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: #e50914;
    }
    .recommendations {
        font-size: 20px;
        color: #333333;
        padding-left: 20px;
    }
    .stButton > button {
        background-color: #e50914;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Loading files
cosine_sim = joblib.load('cosine_similarity.pkl')
indices = joblib.load('indices.pkl')
df = pd.read_csv('netflix_dataset_preprocessed.csv')

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices.get(title)
    if idx is None:
        return []
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 similar movies
    movie_indices = [i[0] for i in sim_scores]
    
    return df['title'].iloc[movie_indices].tolist()

# Application
st.markdown('<div class="title">🎬 Netflix Movie Recommender</div>', unsafe_allow_html=True)
st.write("Find 5 similar movies you might like!")

# Dropdown list to select movies
movie_list = df['title'].sort_values().unique()
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_movie)
    if recommendations:
        st.subheader(f"Movies similar to: {selected_movie}")
        for idx, movie in enumerate(recommendations, 1):
            st.markdown(f"<div class='recommendations'>{idx}. {movie}</div>", unsafe_allow_html=True)
    else:
        st.error("No recommendations found for the selected movie.")
