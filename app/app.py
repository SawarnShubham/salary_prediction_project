import streamlit as st
import joblib
import pandas as pd

# Load saved model
model = joblib.load("models/linear_regression.pkl")

st.title("Salary Prediction App")

st.write("Predict Salary based on Years of Experience")

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.1
)

if st.button("Predict Salary"):
    input_data = pd.DataFrame({
        "YearsExperience": [experience]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")