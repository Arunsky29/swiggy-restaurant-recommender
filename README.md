🍴 Swiggy Restaurant Recommendation System

A machine learning–powered web app built with Streamlit that recommends restaurants based on your preferences — including city, cuisine, rating, cost, and more.

🚀 Overview

The Swiggy Restaurant Recommendation System uses OneHotEncoding, Cosine Similarity, and a cleaned dataset of Swiggy restaurant data to suggest the most relevant dining options for users.

Users simply select preferences (like city, cuisine, and rating) — and the app intelligently recommends top restaurants nearby with their details, links, and ratings.

🧠 Features

✅ Personalized Recommendations — Uses ML similarity scoring to match restaurants to user preferences.
✅ Interactive Streamlit Interface — Built with a clean sidebar-driven design.
✅ Fast & Lightweight — Optimized to run locally without high memory usage.
✅ Dynamic Filtering — Choose city, cuisine, cost range, and rating threshold.
✅ Swiggy Links — Each restaurant links directly to its Swiggy page.

🧩 Tech Stack
Category	Tools / Libraries
Frontend / UI	Streamlit
Backend / ML	Scikit-learn (OneHotEncoder, Cosine Similarity)
Data Handling	Pandas, NumPy
Data Source	Swiggy Dataset (CSV)
Language	Python 3.12
🧱 Project Structure
swiggy-restaurant-recommender/
│
├── cleaned_data.csv             # Cleaned restaurant dataset
├── encoded_data.csv             # One-hot encoded data for ML
├── encoder.pkl                  # Stored encoder + column metadata
├── Swiggy.py                    # Main Streamlit app file
├── Swiggy_Recommendation.ipynb  # Colab notebook for data preprocessing
├── requirements.txt             # Dependencies for installation
├── assets/
│   └── app_preview.png          # Screenshot of the app UI
└── README.md                    # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/swiggy-restaurant-recommender.git
cd swiggy-restaurant-recommender

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run Swiggy.py

4️⃣ Open in Browser

👉 http://localhost:8501
