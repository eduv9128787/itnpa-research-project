
import streamlit as st
import joblib
import re
from pathlib import Path
from nltk.corpus import stopwords

# Load saved model components
model_dir = Path(__file__).resolve().parent

tfidf = joblib.load(model_dir / "tfidf_vectorizer.pkl")
selector = joblib.load(model_dir / "feature_selector.pkl")
model = joblib.load(model_dir / "random_forest_model.pkl")

# Preprocessing consistent with model training
stop_words = set(stopwords.words("english")) - {"no", "not", "nor"}

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = " ".join(
        word for word in text.split()
        if word not in stop_words
    )
    return text

# Web interface
st.set_page_config(
    page_title="Research Abstract Classifier",
    page_icon="🔬"
)

st.title("🔬 Research Abstract Classifier")

st.write(
    "Enter a research abstract to classify it as "
    "AI Research or Classical Research."
)

abstract = st.text_area(
    "Research Abstract",
    height=200,
    placeholder="Paste your research abstract here..."
)

if st.button("Classify Abstract"):

    if not abstract.strip():
        st.warning("Please enter a research abstract.")

    else:
        cleaned_text = preprocess_text(abstract)

        features = tfidf.transform([cleaned_text])
        selected_features = selector.transform(features)

        prediction = model.predict(selected_features)[0]

        if prediction == "ai":
            st.success("Prediction: AI Research")
        else:
            st.success("Prediction: Classical Research")
