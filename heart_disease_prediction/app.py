import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model, feature columns, scaler
model = joblib.load("heart_disease_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")
scaler = joblib.load("scaler.pkl")

st.title("❤️ Heart Disease Prediction App")
st.write("Fill out the form below to get a prediction.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex_display = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex_display == "Male" else 0

cp_display = st.selectbox("Chest Pain Type", [
    "Typical Angina", 
    "Atypical Angina", 
    "Non-anginal Pain", 
    "Asymptomatic"
])
cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
cp = cp_map[cp_display]

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0, max_value=10.0, value=1.0)

slope_display = st.selectbox("Slope of peak exercise ST segment", ["Upsloping", "Flat", "Downsloping"])
slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slope = slope_map[slope_display]

ca = st.selectbox("Number of major vessels (0–3)", [0, 1, 2, 3])

thal_display = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])
thal_map = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}
thal = thal_map[thal_display]

# Prepare dataframe (same format as scaler training)
input_dict = {
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "thalach": thalach,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

input_df = pd.DataFrame([input_dict])

numeric_cols = scaler.feature_names_in_ 
input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])


for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[feature_columns]

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]
    
    st.write(f"**Probability of heart disease:** {proba:.2%}")
    
    if prediction == 1:
        st.error("🚨 High risk of heart disease.")
    else:
        st.success("✅ Low risk of heart disease.")
