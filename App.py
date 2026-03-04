import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import requests
import html

st.set_page_config(page_title="Anime Recommender", layout="wide)
@st.cache_data
def load_data():
    anime = pd.read_csv("anime (2).csv")
    anime['genre'] = anime['genre'].fillna('')
    anime['name'] = anime['name'].apply(html.unescape).str.strip()
    return anime
@st.cache_data
def create_similarity_matrix(anime_df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(anime_df['genre'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

@st.cache_data(show_spinner=False)
def fetch_poster(anime_name):
    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"

    try:
        response = requests.get(url)
        data = response.json()

        if data["data"]:
            return data["data"][0]["images"]["jpg"]["image_url"]
        return None
    except:
        return None
def recommend_content(title, anime_df, cosine_sim, top_n=5):

    anime_df['name_lower'] = anime_df['name'].str.lower()
    title = title.lower()

    matches = anime_df[anime_df['name_lower'].str.contains(title)]

    if matches.empty:
        return None

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    anime_indices_top = [i[0] for i in sim_scores]

    return anime_df.iloc[anime_indices_top]
st.title("🎌 Anime Recommender System")
st.markdown("Get Top 5 Similar Anime Recommendations Instantly 🚀")

anime_df = load_data()
cosine_sim = create_similarity_matrix(anime_df)

user_input = st.text_input("Enter Anime Title:")

if user_input:
    recommendations = recommend_content(user_input.strip(), anime_df, cosine_sim)

    if recommendations is None:
        st.warning("❌ Anime not found! Please check spelling.")
    else:
        st.success("🔥 Top 5 Anime You Might Enjoy")

        cols = st.columns(5)

        for idx, (index, row) in enumerate(recommendations.iterrows()):
            poster = fetch_poster(row['name'])

            with cols[idx]:
                if poster:
                    st.image(poster)
                st.caption(row['name'])
