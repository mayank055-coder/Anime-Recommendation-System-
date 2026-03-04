🎌 Anime Recommendation System

A production-ready Content-Based Anime Recommendation System built using TF-IDF Vectorization and Cosine Similarity, deployed with Streamlit and integrated with live poster fetching via the Jikan (MyAnimeList) API.

🚀 Live Demo
https://anime-recommendation-webai.streamlit.app

📌 Overview
This project recommends the Top 5 most similar anime based on genre similarity using Natural Language Processing techniques.
The system:
Processes anime genre data
Converts text into numerical vectors using TF-IDF
Computes similarity using Cosine Similarity
Displays top recommendations with live posters
Runs on an interactive Streamlit web interface

Try searching for:
Naruto
Attack on Titan
Demon Slayer: Kimetsu no Yaiba

🧠 Problem Statement

With thousands of anime titles available, users often struggle to discover similar content based on their preferences.
This system solves that problem using a content-based filtering approach, focusing on genre similarity instead of collaborative user data.

🏗 Architecture

Step 1 — Data Preprocessing
Load dataset
Clean missing genre values
Normalize anime titles

Step 2 — Feature Engineering

Apply TF-IDF on genre column
Transform text into numerical feature vectors

Step 3 — Similarity Computation

Generate cosine similarity matrix
Rank similar anime titles

Step 4 — UI Rendering

Accept user input
Fetch top 5 recommendations
Display posters via Jikan API
Render results in responsive 5-column layout

🛠 Tech Stack
Technology	Purpose
Python	Core Programming
Pandas	Data Processing
Scikit-learn	TF-IDF & Cosine Similarity
Streamlit	Web Application
Requests	API Calls
Jikan API	Live Poster Data
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

Push project to GitHub
Go to Streamlit Cloud
Connect repository
Select app.py
Deploy

Ensure:

requirements.txt
streamlit
pandas
scikit-learn
requests

runtime.txt
python-3.11

🎯 Key Features

✔ Content-Based Recommendation
✔ TF-IDF Vectorization
✔ Cosine Similarity Ranking
✔ Top 5 Smart Recommendations
✔ Case-Insensitive Search
✔ Live Poster Fetching (No API Key Required)
✔ Optimized for Streamlit Cloud Deployment
✔ Clean & Responsive UI

🚀 Performance Optimization

Cached similarity matrix using st.cache_resource
Limited dataset size for cloud memory optimization
Efficient API calls with caching
Lightweight deployment architecture

📈 Future Enhancements

Add rating & popularity metrics
Display similarity percentage
Implement fuzzy search
Hybrid recommendation system
User preference personalization

👨‍💻 Author

Mayank Gupta
BCA Student | Aspiring Data Analyst | ML Enthusiast

LinkedIn: in/mayank-gupta-data-analyst

GitHub:https://github.com/mayank055-coder
