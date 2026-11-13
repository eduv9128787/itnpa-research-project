# Research Abstract Classifier — Deployment Guide

## Overview
This Streamlit application classifies research abstracts as
AI Research or Classical Research using a trained Random Forest model.

## Requirements
- Python 3.10
- pip

## Installation

1. Download or clone the GitHub repository.
2. Open Terminal and navigate to the deployment folder.
3. Install the required packages:

   pip install -r requirements.txt

4. Download the NLTK stopwords dataset:

   python -m nltk.downloader stopwords

## Run the Application

From inside the deployment folder, run:

   python -m streamlit run app.py

Open http://localhost:8501 in your browser.

## How to Use
1. Paste a research abstract into the text box.
2. Click "Classify Abstract".
3. View the predicted category.

## Model Components
- tfidf_vectorizer.pkl — TF-IDF feature extraction
- feature_selector.pkl — Chi-square feature selection
- random_forest_model.pkl — Trained Random Forest classifier

## Performance
The improved model achieved 93.42% test accuracy.

## Notes
The model predicts one of two research categories.
Predictions are based on the training dataset and may not
generalise to every research abstract.
