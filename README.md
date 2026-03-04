🎌 Anime Recommendation System

A Production-Ready Content-Based Anime Recommendation System built using TF-IDF Vectorization and Cosine Similarity, deployed with Streamlit Cloud, and integrated with live poster fetching via the Jikan (MyAnimeList) API.

🔗 Live Application:
https://anime-recommendation-webai.streamlit.app

📌 Executive Overview

With thousands of anime titles available globally, discovering similar content based on user preference can be overwhelming.

This project solves that problem using a Content-Based Filtering Approach, leveraging Natural Language Processing (NLP) techniques to recommend anime based on genre similarity — without requiring user history or collaborative data.

The system:

Processes anime genre metadata

Converts textual genres into numerical vectors using TF-IDF

Computes similarity scores using Cosine Similarity

Returns the Top 5 Most Relevant Anime

Dynamically fetches posters using the Jikan API

Runs on a clean and interactive Streamlit web interface

🧠 Problem Statement

Traditional recommendation systems often rely on user behavior data (collaborative filtering), which is not always available.

This project implements a Content-Based Recommendation System, where recommendations are generated based solely on:

Genre similarity

Text feature extraction

Mathematical similarity scoring

This makes the system:

Lightweight

Scalable

Cold-start friendly

Cloud-deployable

🏗 System Architecture
1️⃣ Data Preprocessing

Load dataset (anime.csv)

Handle missing genre values

Normalize and clean anime titles

2️⃣ Feature Engineering

Apply TF-IDF Vectorization on the genre column

Convert text data into numerical feature vectors

3️⃣ Similarity Computation

Compute Cosine Similarity Matrix

Rank anime titles based on similarity scores

4️⃣ UI Rendering (Streamlit Layer)

Accept user search input

Retrieve Top 5 similar anime

Fetch live posters from Jikan API

Display recommendations in responsive column layout

🛠 Tech Stack
Technology	Purpose
Python	Core Programming
Pandas	Data Processing
Scikit-Learn	TF-IDF & Cosine Similarity
Streamlit	Web Application Framework
Requests	API Handling
MyAnimeList	Anime Metadata Source
📂 Project Structure
anime-recommendation-system/
│
├── app.py
├── anime.csv
├── requirements.txt
├── runtime.txt
└── README.md
⚙ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/anime-recommendation-system.git
cd anime-recommendation-system
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
☁ Deployment (Streamlit Cloud)

This project is optimized for deployment on:

👉 Streamlit Cloud

Deployment Steps:

Push repository to GitHub

Connect repository in Streamlit Cloud

Select app.py

Deploy

Required Files:

requirements.txt

streamlit
pandas
scikit-learn
requests

runtime.txt

python-3.11
🎯 Key Features

✔ Content-Based Filtering
✔ TF-IDF Vectorization
✔ Cosine Similarity Ranking
✔ Top 5 Smart Recommendations
✔ Case-Insensitive Search
✔ Live Poster Fetching (No API Key Required)
✔ Streamlit Cloud Optimized
✔ Clean & Responsive UI
✔ Cached Computations for Performance

🚀 Performance Optimization

Cached similarity matrix using st.cache_resource

Optimized dataset size for cloud memory limits

Efficient API calls with lightweight JSON parsing

Fast vector similarity computation

📈 Future Enhancements

Add Rating & Popularity Filtering

Display Similarity Percentage

Implement Fuzzy Search

Hybrid Recommendation System

User Preference Personalization

Deploy with Docker for production scaling

👨‍💻 Author

Mayank Gupta
BCA Student | Aspiring Data Analyst | ML Enthusiast

🔗 LinkedIn:
https://www.linkedin.com/in/mayank-gupta-data-analyst

🔗 GitHub:
https://github.com/mayank055-coder

⭐ If You Like This Project

Consider giving it a ⭐ on GitHub — it helps showcase the project to recruiters and supports open-source growth.
