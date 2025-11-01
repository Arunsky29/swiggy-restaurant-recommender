
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    clean_df = pd.read_csv("C:/Users/arunk/Downloads/cleaned_data.csv")
    encoded_df = pd.read_csv("C:/Users/arunk/Downloads/encoded_data.csv")
    
    with open("C:/Users/arunk/Downloads/encoder.pkl", "rb") as f:
        meta = pickle.load(f)
    
    encoder = meta["encoder"]
    categorical_cols = meta["categorical_cols"]
    numeric_cols = meta["numeric_cols"]
    return clean_df, encoded_df, encoder, categorical_cols, numeric_cols


clean_df, encoded_df, encoder, categorical_cols, numeric_cols = load_data()

st.set_page_config(
    page_title="Swiggy Restaurant Recommendation System 🍽️",
    layout="wide"
)

st.title("🍴 Swiggy Restaurant Recommendation System")
st.markdown("Get personalized restaurant suggestions based on your preferences!")

st.sidebar.header("User Preferences")

city = st.sidebar.selectbox("Select City", sorted(clean_df["city"].dropna().unique()))
cuisine = st.sidebar.selectbox("Select Cuisine", sorted(clean_df["cuisine"].dropna().unique()))

rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 4.0, 0.1)
rating_count = st.sidebar.number_input("Minimum Rating Count", min_value=0, value=50)
cost = st.sidebar.number_input("Approximate Cost for Two (₹)", min_value=0, value=300)

user_input = {
    "city": city,
    "cuisine": cuisine,
    "rating": rating,
    "rating_count": rating_count,
    "cost": cost
}

def build_user_vector(user_input):
    num_values = [float(user_input.get(col, 0)) for col in numeric_cols]
    cat_values = [user_input.get(col, "Unknown") for col in categorical_cols]
    cat_encoded = encoder.transform([cat_values])[0]
    user_vector = np.concatenate([num_values, cat_encoded])
    return user_vector


def recommend_restaurants(user_input, top_n=5):
    user_vector = build_user_vector(user_input)
    similarities = cosine_similarity([user_vector], encoded_df)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    recommendations = clean_df.iloc[top_indices][
        ['name', 'city', 'cuisine', 'rating', 'cost', 'address', 'link']
    ].copy()
    recommendations["similarity_score"] = similarities[top_indices]
    return recommendations

if st.sidebar.button("Get Recommendations 🍽️"):
    st.subheader("✨ Recommended Restaurants for You ✨")
    results = recommend_restaurants(user_input, top_n=5)
    
    for i, row in results.iterrows():
        with st.container():
            st.markdown(f"### 🍛 {row['name']}")
            st.markdown(f"**📍 City:** {row['city']}")
            st.markdown(f"**🍴 Cuisine:** {row['cuisine']}")
            st.markdown(f"**⭐ Rating:** {row['rating']} | 💰 Cost:** ₹{row['cost']}**")
            st.markdown(f"**📍 Address:** {row['address']}")
            st.markdown(f"[🔗 View on Swiggy]({row['link']})")
            st.markdown("---")

else:
    st.info("👈 Select your preferences in the sidebar and click **Get Recommendations 🍽️**")

st.markdown("---")
st.caption("Developed by Arunkumar • Swiggy Recommendation System (Streamlit + ML)")
