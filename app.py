import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# -------------------------------
# Project folder
# -------------------------------
project_folder = r"C:\Users\dhruv\movie recommendation system"

st.title("🎬 Movie Recommendation System")
#st.write("Current working directory:", os.getcwd())
#st.write("Project folder:", project_folder)

# -------------------------------
# Load CSV
# -------------------------------
def load_data(csv_file="movies_processed.csv", nrows=None):
    df_path = os.path.join(project_folder, csv_file)
    if not os.path.exists(df_path):
        st.error(f"File not found: {csv_file}")
        return None
    df = pd.read_csv(df_path, nrows=nrows)
    if 'poster_path' not in df.columns:
        df['poster_path'] = None
    if 'overview' not in df.columns:
        df['overview'] = ""
    df["title_lower"] = df["title"].str.lower()
    return df

df = load_data(nrows=10000)
if df is None:
    st.stop()

# -------------------------------
# Load similarity matrix
# -------------------------------
def load_similarity(pkl_file="similarity.pkl", nrows=None):
    sim_path = os.path.join(project_folder, pkl_file)
    if not os.path.exists(sim_path):
        st.error(f"File not found: {pkl_file}")
        return None
    with open(sim_path, "rb") as f:
        similarity_full = pickle.load(f)
    if nrows is not None:
        similarity_full = similarity_full[:nrows, :nrows]
    return similarity_full

similarity = load_similarity(nrows=10000)
if similarity is None:
    st.stop()

# -------------------------------
# Searchable movie input
# -------------------------------
choice = st.text_input("Type a movie name (case-insensitive, partial match works):").lower()

# -------------------------------
# Recommendation function
# -------------------------------
def recommend(movie):
    matches = df[df["title_lower"].str.contains(movie)]
    if matches.empty:
        st.error("Movie not found in dataset. Try different spelling!")
        return None, []
    idx = matches.index[0]
    distances = list(enumerate(similarity[idx]))
    movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    recommended_rows = [df.iloc[i[0]] for i in movies]
    return df.iloc[idx], recommended_rows

# -------------------------------
# Show recommendations
# -------------------------------
BASE_URL = "https://image.tmdb.org/t/p/w500"

if st.button("Recommend") and choice:
    original, rec_rows = recommend(choice)
    if original is not None:
        st.write("### You searched for:")
        st.subheader(original["title"])
        if original["poster_path"]:
            try:
                st.image(BASE_URL + original["poster_path"], width=150)
            except:
                st.write("Poster not available")
        if original["overview"]:
            st.write(original["overview"])
        st.write("---")
    
    if rec_rows:
        st.write("### Recommended Movies:")
        for row in rec_rows:
            st.subheader(row["title"])
            if row["poster_path"]:
                try:
                    st.image(BASE_URL + row["poster_path"], width=150)
                except:
                    st.write("Poster not available")
            if row["overview"]:
                st.write(row["overview"])
            st.write("---")
