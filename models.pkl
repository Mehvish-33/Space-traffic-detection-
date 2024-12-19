import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load the dataset (replace with your actual dataset path)
data = pd.read_csv('processed_space_traffic.csv')  # Make sure to replace this with your dataset

# Encode Traffic Density Category
label_encoder = LabelEncoder()
data['Traffic_Density_Category'] = label_encoder.fit_transform(data['Traffic_Density_Category'])

# Features and Target
X = data.drop(columns=['Traffic_Density', 'Traffic_Density_Category'])
y = data['Traffic_Density']

# Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)

svm_model = SVR()
svm_model.fit(X_train, y_train)

rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)

with open('dt_model.pkl', 'wb') as f:
    pickle.dump(dt_model, f)

with open('svm_model.pkl', 'wb') as f:
    pickle.dump(svm_model, f)

with open('rf_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

print("Models saved successfully.")
