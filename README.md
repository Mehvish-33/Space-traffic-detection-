# 🚀 Space Traffic Detection & Prediction 🚀

## Project Overview 🌌

This project aims to predict **space traffic density** based on various features related to space objects and their activities. The prediction is performed using **Ridge Regression** to forecast traffic density based on input data such as time, object type, location, and peak time hours.

It provides an **interactive web application** using **Streamlit**, allowing users to input parameters and get real-time predictions. This application serves as a tool to **predict traffic density in space**, which could be useful for space agencies, satellite operators, and researchers involved in space exploration, satellite communication, and space station management.

---

## Key Features 🔑

- **Interactive Web Interface**: Users can input data such as **time**, **object type** (asteroid, satellite, space station, etc.), and **location** to predict traffic density.
- **Predictive Modeling**: The model uses **Ridge Regression** to forecast traffic density, based on historical data.
- **Data Visualization**: The application displays visualizations such as **traffic density plots** and **space-related images**.
- **Customizable Inputs**: Users can customize the **year**, **month**, **day**, **hour**, and more to see the predicted traffic density.

---

## Technologies Used 🛠️

- **Streamlit**: For creating an interactive web application.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For machine learning models (Ridge Regression and Label Encoding).
- **Plotly**: For interactive visualizations and graphs.
- **Matplotlib**: For static visualizations and custom plots.

---

## Setup Instructions 🖥️

### 1. Clone the Repository 📂

```bash
git clone https://github.com/SharvaniDhulipala-DS/Space-Traffic-Detection.git
cd Space-Traffic-Detection
```
## 2. Install Dependencies 📦

To install the required Python libraries, run the following command in your terminal:

```bash
pip install -r requirements.txt
```
## 3. Run the Streamlit Application 🎮

To start the application locally, use the following command:

```bash
streamlit run Streamlit.py
```
## Data & Model 🧑‍💻

The dataset used in this project contains various space traffic parameters such as object types (asteroid, spacecraft, satellite, etc.), time of occurrence, peak hours, and location. Traffic Density is predicted based on this data to help understand traffic patterns and avoid space collisions.

### Model Overview:
The model is trained using **Ridge Regression**, a linear model that is particularly useful for predicting traffic density when there is multicollinearity between features. Ridge regression helps to reduce model complexity and prevent overfitting by applying regularization.

### Data Features:
- **Object Type**: Different types of space objects such as asteroids, spacecraft, and satellites.
- **Time of Occurrence**: Timestamp representing when the space object activity occurred.
- **Peak Hours**: The peak hours of space traffic activity.
- **Location**: Geographical location of space activity, encoded for model prediction.

### Model Training:
- The model has been trained using the above features.
- It uses **Ridge Regression** to predict traffic density based on the input data.
- The model has been tuned to ensure that it provides reliable predictions across a variety of conditions.

### Traffic Density Categorization:
The predicted traffic density is categorized based on different features such as time, object type, and location. Traffic density is represented visually using various graphs to help understand the trends and patterns in space traffic.

### Traffic Density Prediction:
- The **Ridge Regression** model predicts traffic density based on the provided input data (such as time and object type).
- The output is a numeric value indicating the level of space traffic density, which can help in planning and collision avoidance.

## Visualization 📊

### Example Prediction Graph 📈
The application allows users to visualize predicted traffic density based on the input values like time and object type. The user can select different parameters, and the model will return the predicted traffic density.

### Space-Themed Background & Images 🌠

#### Interactive Visuals:
The app includes space-related images and beautiful visualizations to make the experience more engaging.

#### Custom Space Images:
A space-themed background is used in the UI to create a better user experience. ![Space-themed background](https://media.licdn.com/dms/image/v2/D5612AQGGi6fuWx9fhA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1692084977968?e=2147483647&v=beta&t=L-cD-2JmNn1NbNbbRbp_wpKDLmbGTGp_xmyn9Btfb0w)

### Interactive Charts:
- **Traffic Density Over Time**: A line plot showing how traffic density varies over time, with different object types.
- **Correlation Heatmap**: A heatmap to show how different features are correlated with traffic density.

## Application Walkthrough 🚶‍♀️

- **Homepage**: Displays the title and a brief description of space traffic prediction.
- **Input Parameters**: Users input the year, month, day, hour, peak hour, location, and object types (satellite, asteroid, etc.).
- **Model Prediction**: After inputting data, users click the "Predict Traffic Density" button to get the predicted traffic density.
- **Visualization**: The app generates interactive graphs showing the traffic density predictions along with relevant plots and images.

## Screenshots 📸

**Space Traffic Prediction Interface**:
- Input fields for customizing the traffic prediction parameters.
- Predicted output displayed dynamically after input.
## Example Usage 🎯

### User Input:
- Year: 2025
- Month: 1
- Day: 15
- Hour: 12
- Peak Time Hour: 1
- Location Encoded: 5
- Object Type: Spacecraft

### Output:
- **Predicted Traffic Density**: 7.56 (This is the output that will be predicted by the Ridge Regression model based on input parameters).

---

## Conclusion 💡

The **Space Traffic Detection** app is a tool for predicting space traffic density, which can aid space mission planning, satellite coordination, and collision avoidance. It uses machine learning techniques to provide accurate predictions based on the provided features. With its intuitive interface and predictive power, it can help organizations prepare for traffic management in space.

---

## Future Enhancements 🔮
- Integration with real-time satellite data for up-to-date predictions.
- Expanding the model to handle more features like satellite orbit data and communication patterns.
- Adding a feature to visualize predicted traffic density on a global map.

---

## Contribute 🤝

Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions, bug fixes, or enhancements.
