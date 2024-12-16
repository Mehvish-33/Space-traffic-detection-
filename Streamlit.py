import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

# Load space-themed image
st.image("https://media.licdn.com/dms/image/v2/D5612AQGGi6fuWx9fhA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1692084977968?e=2147483647&v=beta&t=L-cD-2JmNn1NbNbbRbp_wpKDLmbGTGp_xmyn9Btfb0w", caption="Space Traffic Prediction", use_column_width=True)

# Header and description
st.title("Space Traffic Density Prediction 🚀")
st.write("""
This app predicts the space traffic density based on various parameters such as the year, month, day, hour, and type of space object. 
Make sure to input the details correctly to get the predicted traffic density.
""")

# File Upload (User can upload their own file)
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    # Default file path (if no file is uploaded)
    file_path = './processed_space_traffic.csv'
    data = pd.read_csv(file_path)

# Show basic dataset info
if st.checkbox('Show Dataset Info'):
    st.write("Dataset Preview:")
    st.dataframe(data.head())

# Encode Traffic Density Category
label_encoder = LabelEncoder()
data['Traffic_Density_Category'] = label_encoder.fit_transform(data['Traffic_Density_Category'])

# Features and Target
X = data.drop(columns=['Traffic_Density', 'Traffic_Density_Category'])
y = data['Traffic_Density']

# Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge Regression Model
ridge_model = Ridge(alpha=100)
ridge_model.fit(X_train, y_train)

# Show Distribution of Traffic Density
st.subheader("Traffic Density Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data['Traffic_Density'], kde=True, color="blue", ax=ax)
ax.set_title("Distribution of Traffic Density")
st.pyplot(fig)

# User Input Section
st.subheader("Input Features for Prediction")
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

# Prediction Button
if st.button("Predict Traffic Density"):
    prediction = ridge_model.predict(input_data)
    st.markdown(f"### Predicted Traffic Density: **{prediction[0]:.2f}**")

    # Additional Visualization: Traffic Density vs Time (for instance)
    st.subheader("Traffic Density Prediction Visualization")
    fig = px.scatter(data, x="Year", y="Traffic_Density", color="Traffic_Density_Category",
                     title="Traffic Density vs Year", labels={"Traffic_Density": "Traffic Density"})
    st.plotly_chart(fig)

# Add Space-themed Background for Streamlit App
st.markdown("""
<style>
    .reportview-container {
        background-image: url("https://media.licdn.com/dms/image/v2/D5612AQGGi6fuWx9fhA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1692084977968?e=2147483647&v=beta&t=L-cD-2JmNn1NbNbbRbp_wpKDLmbGTGp_xmyn9Btfb0w");
        background-size: cover;
    }
</style>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
---
Built with ❤️ by Sharvani
""")
