# 🎬 BrainBytes Movie Recommendation System

This project is an intelligent movie recommendation system developed by **BrainBytes**, designed to deliver personalized film suggestions using machine learning and interactive web technologies.

 Overview

The system leverages a Kaggle dataset of movie ratings and metadata to build a hybrid recommendation engine. It combines collaborative filtering and content-based filtering to suggest movies tailored to user preferences. The final application is deployed using **Streamlit**, offering a sleek and responsive user interface.

## 🧠 Tech Stack

- **Python**
- **Jupyter Notebook** – for data exploration, preprocessing, and model development
- **Streamlit** – for building the interactive web app
- **Pandas, Scikit-learn, Numpy** – for data manipulation and modeling
- **Pickle** – for saving processed data and models

## 📁 Project Structure

| File/Notebook              | Description |
|---------------------------|-------------|
| `app.py`                  | Main Streamlit app that loads data and serves movie recommendations through a web interface. |
| `movie_list.pkl`          | Serialized file containing processed movie metadata used for fast lookup and recommendation logic. |
| `processed_movies.ipynb`  | Handles data cleaning, feature engineering, and preparation of the movie dataset. |
| `recommender system.ipynb`| Implements collaborative and content-based filtering models to generate recommendations. |
| `movie system setup.ipynb`| Sets up the environment, loads datasets, and connects various components of the system. |

## 📊 Dataset

The system uses a publicly available **Kaggle dataset** containing:
- Movie titles and genres
- User ratings
- Metadata such as release year and cast

## 💡 Features

- Personalized movie recommendations based on user input
- Hybrid filtering techniques for improved accuracy
- Interactive UI with real-time suggestions
- Scalable design for integration with streaming platforms


