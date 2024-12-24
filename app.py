
import pandas as pd
import streamlit as st
import pickle
import numpy as np

# Space-Themed Header Image and Title
st.image(
    "https://media.licdn.com/dms/image/v2/D5612AQGGi6fuWx9fhA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1692084977968?e=2147483647&v=beta&t=L-cD-2JmNn1NbNbbRbp_wpKDLmbGTGp_xmyn9Btfb0w",
    caption="Space Traffic Prediction",
    use_container_width=True,
)

st.markdown(
    """
    <h1 style='text-align: center; color: #1e81b0;'>
    🚀 Space Traffic Density Prediction 🚀
    </h1>
    <p style='text-align: center; font-size: 16px;'>
    Predict the density of space traffic based on year, month, day, hour, location, and space object type.
    </p>
    <p style='text-align: center; font-size: 14px;'>
    Check out the source code on <a href="https://github.com/SharvaniDhulipala-DS/Space-Traffic-Detection" target="_blank">GitHub</a>!
    </p>
    """,
    unsafe_allow_html=True,
)

# Load pre-trained models
with open('dt_model.pkl', 'rb') as f:
    dt_model = pickle.load(f)

with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

# Model Selection for Prediction
st.subheader("Select the Model for Prediction 🚀")

model_selection = st.radio(
    "Choose a model to predict traffic density:",
    ("Decision Tree", "SVM", "Random Forest")
)

# Define the columns in the model for input data, these should match your training data
columns = [
    'Year', 'Month', 'Day', 'Hour', 'Peak_Time_Hour', 'Location_Encoded',
    'Object_Type_Asteroid Mining Ship', 'Object_Type_Manned Spacecraft',
    'Object_Type_Satellite', 'Object_Type_Scientific Probe', 'Object_Type_Space Debris',
    'Object_Type_Space Station'
]

# Input Features for Prediction
st.subheader("Input Features for Prediction 🛸")

# Neatly structured input for year, month, day, hour, peak_time_hour, location
col1, col2 = st.columns(2)
with col1:
    year = st.number_input("Year", min_value=2020, max_value=2030, value=2024, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, value=1, step=1)
    day = st.number_input("Day", min_value=1, max_value=31, value=1, step=1)

with col2:
    hour = st.number_input("Hour", min_value=0, max_value=23, value=12, step=1)
    peak_time_hour = st.number_input("Peak Time Hour", min_value=0, max_value=3, value=0, step=1)

# Location and Space Object Type Selection
st.subheader("Select Location and Space Object Type 🌍🛸")

col1, col2 = st.columns(2)

# Location Selection in Column 1
location_options = {
    "Lagrange Point L2": 1,
    "Orbit LEO": 4,
    "Mars Transfer Orbit": 2,
    "Lagrange Point L1": 0,
    "Orbit GEO": 3,
    "Orbit MEO": 5,
}

with col1:
    location = st.radio("Select Location:", list(location_options.keys()), index=0)

# Object Type Selection in Column 2
object_type = st.radio(
    "Select Space Object Type:",
    [
        "Asteroid Mining Ship",
        "Manned Spacecraft",
        "Satellite",
        "Scientific Probe",
        "Space Debris",
        "Space Station",
    ],
    index=0,
)

# Convert selection into binary format for object type input
object_type_data = {
    "Asteroid Mining Ship": [1, 0, 0, 0, 0, 0],
    "Manned Spacecraft": [0, 1, 0, 0, 0, 0],
    "Satellite": [0, 0, 1, 0, 0, 0],
    "Scientific Probe": [0, 0, 0, 1, 0, 0],
    "Space Debris": [0, 0, 0, 0, 1, 0],
    "Space Station": [0, 0, 0, 0, 0, 1],
}

selected_object = object_type_data[object_type]

# Prepare Input Data
input_data = pd.DataFrame(
    {
        "Year": [year],
        "Month": [month],
        "Day": [day],
        "Hour": [hour],
        "Peak_Time_Hour": [peak_time_hour],
        "Location_Encoded": [location_options[location]],
        "Object_Type_Asteroid Mining Ship": [selected_object[0]],
        "Object_Type_Manned Spacecraft": [selected_object[1]],
        "Object_Type_Satellite": [selected_object[2]],
        "Object_Type_Scientific Probe": [selected_object[3]],
        "Object_Type_Space Debris": [selected_object[4]],
        "Object_Type_Space Station": [selected_object[5]],
    }
)

# Prediction Button
if st.button("Predict Traffic Density 🚀"):
    try:
        if model_selection == "Decision Tree":
            model = dt_model
        elif model_selection == "SVM":
            model = svm_model
        else:
            model = rf_model

        # Make prediction using the selected model
        traffic_density_prediction = model.predict(input_data)
        st.markdown(
            f"### Predicted Traffic Density: **{traffic_density_prediction[0]:.2f}** 🚀",
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(f"Error: {e} 😞")
