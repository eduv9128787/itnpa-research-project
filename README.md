# ITNPA Research Project

## Project Overview
This project applies Natural Language Processing (NLP) and
Machine Learning techniques to classify, summarise and
analyse research documents.

The project covers Questions 1–4 and includes datasets,
Jupyter Notebook analyses, visualisations and a Streamlit
web application.

## Question 1: Research Abstract Classification
Research abstracts were preprocessed and converted into
numerical features using TF-IDF.

A Logistic Regression classifier was trained to distinguish
between AI Research and Classical Research.

Results:
- Training accuracy: 90.86%
- Testing accuracy: 88.16%

## Question 2: Model Comparison, Improvement and Deployment
Four additional classification algorithms were evaluated:
- Multinomial Naive Bayes
- Linear Support Vector Machine
- Random Forest
- Decision Tree

The improved Random Forest model used:
- TF-IDF with unigrams and bigrams
- Chi-square feature selection
- Random Forest classification

Best testing accuracy: 93.42%

The trained model was deployed using Streamlit.

## Question 3: Research Document Analysis
Five research articles were extracted from a ZIP archive
and preprocessed using tokenisation, stopword removal
and lemmatisation.

The analysis included:
- Text cleaning and preprocessing
- TF-IDF-based extractive summarisation
- TextRank-based multi-document summarisation
- Word-frequency visualisations
- Thematic analysis visualisations

## Question 4: Topic Modelling and Visualisation
Latent Dirichlet Allocation (LDA) was used to identify
three topics across the research documents.

The analysis includes:
- Top words associated with each topic
- Topic distributions across documents
- Topic-word visualisations
- Document-topic heatmap
- Interactive pyLDAvis Intertopic Distance Map

## Repository Structure
- datasets/ : Original research datasets
- notebooks/ : Jupyter Notebook containing Questions 1–4
- deployment/ : Streamlit application and saved model files
- visualizations/ : Interactive LDA visualisation

## Running the Notebook
1. Download or clone this repository.
2. Open the notebook in the notebooks folder using Jupyter.
3. Install the Python packages required by the notebook.
4. Run the notebook cells in order.

## Running the Web Application
See deployment/README.md for installation and
deployment instructions.

## Notes
The project is intended for academic research and
demonstration purposes. Model predictions and discovered
topics are dependent on the supplied datasets.
