# Salary Prediction using Linear Regression

## Project Overview

This project predicts employee salary based on years of experience using Linear Regression. It demonstrates the complete machine learning workflow from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, model saving, and deployment using Streamlit.

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Streamlit
* Joblib

## Features

* Data loading and preprocessing
* Exploratory Data Analysis (EDA)
* Missing value and duplicate check
* Scatter plot visualization for relationship analysis
* Train-test split for model training
* Linear Regression model building
* Model evaluation using R2 Score and Mean Squared Error (MSE)
* Regression line visualization
* Model saving using Joblib (.pkl)
* Streamlit web app for real-time salary prediction

## Project Structure

salary_prediction_project/
│
├── app/
│   └── app.py
│
├── data/
│   └── salary_data.csv
│
├── models/
│   └── linear_regression.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── src/
│   └── predict.py
│
├── README.md
│
└── requirements.txt

## Run Project

### Install Dependencies

pip install -r requirements.txt

### Run Streamlit App

streamlit run app/app.py

## Output

The user enters years of experience and the model predicts the expected salary instantly using the trained Linear Regression model through the Streamlit web application.

## Conclusion

This project provides strong practical understanding of supervised learning and regression problems. It is a beginner-to-professional level portfolio project for Data Science and Machine Learning roles.
