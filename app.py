import streamlit as st
import joblib
import numpy as np

# Load model + vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# 🎭 App title
st.set_page_config(page_title="Sentiment Analysis App", page_icon="🎭", layout="centered")
st.title("🎭 Sentiment Analysis App")
st.write("Enter a review below and let the AI predict whether it's **Positive** or **Negative** ✨")

# User input
user_input = st.text_area("✍️ Type your review here:")

if st.button("🔍 Predict"):
    if user_input.strip():
        # Transform input
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        probs = model.predict_proba(X_input)[0]  # Get probability scores

        # Map labels to emojis
        if prediction in [1, "pos", "positive"]:
            sentiment = "😊 Positive"
            confidence = probs[1] if len(probs) > 1 else np.max(probs)
        else:
            sentiment = "😞 Negative"
            confidence = probs[0] if len(probs) > 1 else np.max(probs)

        st.success(f"**Predicted Sentiment:** {sentiment}")
        st.info(f"Confidence Score: **{confidence:.2f}**")
    else:
        st.warning("⚠️ Please enter some text for prediction.")
