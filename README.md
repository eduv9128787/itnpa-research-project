# ITNPA Research Project

## Project Overview

This project focuses on using Natural Language Processing (NLP) and Machine Learning to classify, summarise and analyse research papers.

The project covers Questions 1 to 4, where I worked with research abstracts and articles using different machine learning and text analysis techniques. The repository contains the datasets, Jupyter Notebook, visualisations and Streamlit application used in the project.

## Question 1: Research Abstract Classification

For Question 1, I cleaned the research abstracts and used TF-IDF to convert the text into numerical features that a machine learning model could understand.

I then trained a Logistic Regression model to classify the abstracts as either AI Research or Classical Research.

The model achieved:
- Training accuracy: 90.86%
- Testing accuracy: 88.16%

## Question 2: Model Comparison, Improvement and Deployment

For Question 2, I tested four more machine learning models to see whether they could perform better than Logistic Regression.

The models were:
- Multinomial Naive Bayes
- Linear Support Vector Machine (SVM)
- Random Forest
- Decision Tree

Random Forest achieved the highest testing accuracy out of these four models.

I then tried different ways to improve its performance, including hyperparameter tuning, class weighting and feature engineering. The best results came from improving the TF-IDF features by including single words and two-word phrases, followed by chi-squared feature selection.

The improved Random Forest achieved a testing accuracy of 93.42%.

I also created a Streamlit web application where users can enter a research abstract and get a prediction of whether it belongs to AI Research or Classical Research.

## Question 3: Research Document Analysis

For Question 3, I worked with five research articles that were provided in a ZIP file.

The articles were cleaned by removing unnecessary characters and stopwords, followed by text preprocessing.

I used TF-IDF to summarise the first article by selecting important sentences. For the remaining four articles, I used TextRank to create a combined summary.

I also created bar charts to show the most common words and a heatmap to compare the main research themes across the articles.

## Question 4: Topic Modelling and Visualisation

For Question 4, I used Latent Dirichlet Allocation (LDA) to identify the main topics discussed in the five research articles.

I tested models with four and three topics and selected three because the results were easier to understand and represented the articles better.

The three topics focused on:
- Mixed research methods and triangulation
- Developmental research and researcher reflexivity
- Instrument reliability and Cronbach's alpha

I created charts to show the most important words in each topic and a heatmap to show how the topics were distributed across the articles.

I also used pyLDAvis to create an interactive Intertopic Distance Map to explore the topics and their most relevant words.

## Repository Structure

The project files are organised into the following folders:

- `datasets/` - Contains the original datasets used in the project.
- `notebooks/` - Contains the Jupyter Notebook with the code, explanations and results for Questions 1 to 4.
- `deployment/` - Contains the Streamlit application, saved model files and instructions for running the application.
- `visualizations/` - Contains the interactive LDA visualisation.

## Running the Notebook

1. Download or clone the repository.
2. Open the Jupyter Notebook inside the `notebooks` folder.
3. Install the Python libraries used in the notebook.
4. Run the cells in order to view the analysis and results.

## Running the Streamlit Application

Instructions for running the web application can be found in `deployment/README.md`.

## Notes

This project was completed as part of my academic assessment. The models were trained and tested using the provided datasets, so the results may be different when working with other research papers.
