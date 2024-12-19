import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open('dt_model.pkl', 'rb') as f:
    dt_model = pickle.load(f)

with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

# Load dataset for feature engineering
data = pd.read_csv('processed_space_traffic.csv')  # Replace with your actual dataset

# Feature Engineering for input data
X = data.drop(columns=['Traffic_Density', 'Traffic_Density_Category'])
y = data['Traffic_Density']

# Streamlit UI for user input
st.title("Traffic Density Prediction 🌌")
st.write("""
This app predicts traffic density based on various parameters.
""")

# User input
year = st.number_input("Year", min_value=2020, max_value=2030, value=2025)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
day = st.number_input("Day", min_value=1, max_value=31, value=1)
hour = st.number_input("Hour", min_value=0, max_value=23, value=12)
peak_time_hour = st.number_input("Peak Time Hour", min_value=0, max_value=3, value=0)
location_encoded = st.number_input("Location Encoded", min_value=0, max_value=10, value=0)

# Convert input to DataFrame for prediction
input_data = pd.DataFrame({
    'Year': [year],
    'Month': [month],
    'Day': [day],
    'Hour': [hour],
    'Peak_Time_Hour': [peak_time_hour],
    'Location_Encoded': [location_encoded]
})

# Prediction Section
if st.button("Predict Traffic Density"):
    # Get predictions from all models
    dt_prediction = dt_model.predict(input_data)
    svm_prediction = svm_model.predict(input_data)
    rf_prediction = rf_model.predict(input_data)
    
    # Display predictions
    st.write(f"**Decision Tree Prediction:** {dt_prediction[0]:.2f}")
    st.write(f"**SVM Prediction:** {svm_prediction[0]:.2f}")
    st.write(f"**Random Forest Prediction:** {rf_prediction[0]:.2f}")
    
    # Displaying a bar chart for model comparison
    st.subheader("Model Comparison")
    predictions = dt_prediction[0], svm_prediction[0], rf_prediction[0]]
    models = ['Decision Tree', 'SVM', 'Random Forest']
    st.bar_chart(pd.DataFrame({'Model': models, 'Prediction': predictions}))
