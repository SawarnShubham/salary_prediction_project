import joblib
import pandas as pd

# Load saved model
loaded_model = joblib.load("../models/linear_regression.pkl")

# New input data
new_data = pd.DataFrame({
    "YearsExperience": [5]
})

# Prediction
prediction = loaded_model.predict(new_data)

print("Predicted Salary:", prediction[0])