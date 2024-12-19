import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load pre-trained model (Ensure that you have trained your model and saved it as .pkl file)
# You can load the model using pickle
with open('traffic_model.pkl', 'rb') as file:
    dt_model = pickle.load(file)

# Define the columns in the model for input data, these should match your training data
columns = [
    'Year', 'Month', 'Day', 'Hour', 'Peak_Time_Hour', 'Location_Encoded',
    'Object_Type_Asteroid Mining Ship', 'Object_Type_Manned Spacecraft',
    'Object_Type_Satellite', 'Object_Type_Scientific Probe', 'Object_Type_Space Debris',
    'Object_Type_Space Station'
]

# Streamlit UI for user input
st.title("Space Traffic Density Prediction")

# User input
year = st.number_input('Year', min_value=2024, max_value=2025, value=2024)
month = st.number_input('Month', min_value=1, max_value=12, value=10)
day = st.number_input('Day', min_value=1, max_value=31, value=21)
hour = st.number_input('Hour', min_value=0, max_value=23, value=21)
peak_time_hour = st.number_input('Peak Time Hour', min_value=1, max_value=24, value=15)
location_encoded = st.number_input('Location Encoded', min_value=0, max_value=1, value=1)

# Object types (binary encoding for 'True'/'False')
asteroid_mining_ship = st.checkbox('Object Type: Asteroid Mining Ship', value=False)
manned_spacecraft = st.checkbox('Object Type: Manned Spacecraft', value=False)
satellite = st.checkbox('Object Type: Satellite', value=False)
scientific_probe = st.checkbox('Object Type: Scientific Probe', value=False)
space_debris = st.checkbox('Object Type: Space Debris', value=False)
space_station = st.checkbox('Object Type: Space Station', value=False)

# Create input data in a dataframe with the same columns as used in training
input_data = pd.DataFrame({
    'Year': [year],
    'Month': [month],
    'Day': [day],
    'Hour': [hour],
    'Peak_Time_Hour': [peak_time_hour],
    'Location_Encoded': [location_encoded],
    'Object_Type_Asteroid Mining Ship': [1 if asteroid_mining_ship else 0],
    'Object_Type_Manned Spacecraft': [1 if manned_spacecraft else 0],
    'Object_Type_Satellite': [1 if satellite else 0],
    'Object_Type_Scientific Probe': [1 if scientific_probe else 0],
    'Object_Type_Space Debris': [1 if space_debris else 0],
    'Object_Type_Space Station': [1 if space_station else 0]
})

# Ensure the columns match the training dataset
input_data = input_data[columns]

# Make prediction for Traffic Density (Regression)
if st.button("Predict Traffic Density"):
    try:
        traffic_density_prediction = dt_model.predict(input_data)
        st.write(f"Predicted Traffic Density: {traffic_density_prediction[0]:.2f}")
    except Exception as e:
        st.write(f"Error: {e}")

# Make prediction for Traffic Density Category (Classification)
if st.button("Predict Traffic Density Category"):
    try:
        category_prediction = dt_model.predict(input_data)
        st.write(f"Predicted Traffic Density Category: {category_prediction[0]}")
    except Exception as e:
        st.write(f"Error: {e}")
