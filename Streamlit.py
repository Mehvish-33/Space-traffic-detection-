import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

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


# Raw GitHub URL for the default dataset
dataset_url = "https://raw.githubusercontent.com/SharvaniDhulipala-DS/Space-Traffic-Detection/main/processed_space_traffic.csv"

# Ask if the user wants to upload a custom dataset or use the default one
st.subheader("Do you want to upload a custom dataset? 🤔")

# Adding a unique key for the radio button to avoid the 'duplicate ID' issue
upload_option = st.radio("Choose an option:", ["Yes", "No"], key="upload_option")

if upload_option == "Yes":
    # If the user selects 'Yes', allow file upload
    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv", key="file_uploader")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("Custom dataset successfully uploaded! 🚀")
    else:
        st.warning("Please upload a CSV file. 📄")
else:
    # If the user selects 'No', load the default dataset from GitHub
    try:
        data = pd.read_csv(dataset_url)
        st.info("Using default dataset from GitHub. 📊")
    except Exception as e:
        st.error(f"Failed to load default dataset: {e}. Please upload a dataset manually. 😕")

# Proceed with the functionality if dataset is available
if 'data' in locals():
    st.subheader("Traffic Density Distribution")
    try:
        import seaborn as sns
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data['Traffic_Density'], kde=True, color="blue", ax=ax)
        ax.set_title("Distribution of Traffic Density")
        st.pyplot(fig)
    except KeyError:
        st.error("Dataset does not contain 'Traffic_Density' column. Please check your dataset. 🚨")

# Encode Traffic Density Category
if 'data' in locals() and 'Traffic_Density_Category' in data.columns:
    label_encoder = LabelEncoder()
    data['Traffic_Density_Category'] = label_encoder.fit_transform(data['Traffic_Density_Category'])

    # Features and Target
    X = data.drop(columns=['Traffic_Density', 'Traffic_Density_Category'])
    y = data['Traffic_Density']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Ridge Regression Model
    ridge_model = Ridge(alpha=100)
    ridge_model.fit(X_train, y_train)

# Input Features for Prediction
st.subheader("Input Features for Prediction 🛸")

# Neatly structured input
col1, col2 = st.columns(2)
with col1:
    year = st.number_input("Year", min_value=2020, max_value=2030, value=2024, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, value=1, step=1)
    day = st.number_input("Day", min_value=1, max_value=31, value=1, step=1)

with col2:
    hour = st.number_input("Hour", min_value=0, max_value=23, value=12, step=1)
    peak_time_hour = st.number_input("Peak Time Hour", min_value=0, max_value=3, value=0, step=1)

# Location and Space Object Type Selection side by side using st.columns
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
    if 'data' in locals():
        prediction = ridge_model.predict(input_data)
        st.markdown(
            f"### Predicted Traffic Density: **{prediction[0]:.2f}** 🚀",
            unsafe_allow_html=True,
        )
        
