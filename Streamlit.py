import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import LabelEncoder 


# Load the Dataset
file_path = 'processed_space_traffic.csv'
data = pd.read_csv(file_path)

# Encode the Traffic_Density_Category column
label_encoder = LabelEncoder()
data['Traffic_Density_Category'] = label_encoder.fit_transform(data['Traffic_Density_Category'])

# Separate features and target
X = data.drop(columns=['Traffic_Density', 'Traffic_Density_Category'])  # Drop Traffic_Density_Category
y = data['Traffic_Density']

# Train-Test Split (Best ratio: 80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge Regression Model
ridge_model = Ridge(alpha=100)  # Best alpha based on previous tuning
ridge_model.fit(X_train, y_train)

# Streamlit Application
st.title("Space Traffic Density Prediction")
st.write("Provide the input values to predict the traffic density.")

# User Inputs (no change here)
year = st.number_input("Year", min_value=2020, max_value=2030, value=2025, step=1)
month = st.number_input("Month", min_value=1, max_value=12, value=1, step=1)
day = st.number_input("Day", min_value=1, max_value=31, value=1, step=1)
hour = st.number_input("Hour", min_value=0, max_value=23, value=12, step=1)
peak_time_hour = st.number_input("Peak Time Hour", min_value=0, max_value=3, value=0, step=1)
location_encoded = st.number_input("Location Encoded", min_value=0, max_value=10, value=0, step=1)

object_type_asteroid = st.selectbox("Is it an Asteroid Mining Ship?", [0, 1])
object_type_manned = st.selectbox("Is it a Manned Spacecraft?", [0, 1])
object_type_satellite = st.selectbox("Is it a Satellite?", [0, 1])
object_type_probe = st.selectbox("Is it a Scientific Probe?", [0, 1])
object_type_debris = st.selectbox("Is it Space Debris?", [0, 1])
object_type_station = st.selectbox("Is it a Space Station?", [0, 1])

# Prepare Input Data
input_data = pd.DataFrame({
    'Year': [year],
    'Month': [month],
    'Day': [day],
    'Hour': [hour],
    'Peak_Time_Hour': [peak_time_hour],
    'Location_Encoded': [location_encoded],
    'Object_Type_Asteroid Mining Ship': [object_type_asteroid],
    'Object_Type_Manned Spacecraft': [object_type_manned],
    'Object_Type_Satellite': [object_type_satellite],
    'Object_Type_Scientific Probe': [object_type_probe],
    'Object_Type_Space Debris': [object_type_debris],
    'Object_Type_Space Station': [object_type_station]
})

# Prediction
if st.button("Predict Traffic Density"):
    prediction = ridge_model.predict(input_data)
    st.write(f"Predicted Traffic Density: {prediction[0]:.2f}")

