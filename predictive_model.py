import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset (Replace this with a real dataset)
data = {
    "BMI": [18.5, 22.0, 27.5, 30.1, 35.0, 40.2],
    "Age": [22, 30, 45, 50, 60, 65],
    "Exercise_Hours": [5, 3, 2, 1, 0, 0],
    "Health_Risk_Level": ["Low", "Low", "Medium", "Medium", "High", "High"]
}

df = pd.DataFrame(data)

# Features & Target
X = df[['BMI', 'Age', 'Exercise_Hours']]
y = df['Health_Risk_Level']

# Convert target labels into numbers
y = y.map({"Low": 0, "Medium": 1, "High": 2})

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save Model as pkl
with open("bmi_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ BMI prediction model trained and saved as bmi_model.pkl")
