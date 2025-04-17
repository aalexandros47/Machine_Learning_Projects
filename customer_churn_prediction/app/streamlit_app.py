import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉", layout="centered")

# Sidebar Inputs
st.sidebar.header("📋 Customer Input")
age = st.sidebar.slider("Age", 12, 100, 30)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
tenure = st.sidebar.slider("Tenure (Months)", 0, 120, 12)
monthly_charges = st.sidebar.slider("Monthly Charges ($)", 20, 150, 70)

# Gender encoding
gender_num = 1 if gender == "Male" else 0

# Input summary display
st.title("📉 Customer Churn Prediction Dashboard")
st.markdown("This app predicts whether a customer is likely to churn using a machine learning model trained on telecom data.")

with st.expander("📊 View Entered Details"):
    st.write(pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Tenure": [tenure],
        "MonthlyCharges": [monthly_charges]
    }))

# Input data
input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender_num],
    "Tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

# Scale input
input_scaled = scaler.transform(input_data)

# Predict
prediction = model.predict(input_scaled)[0]
prediction_prob = model.predict_proba(input_scaled)[0][1]

# Display Results
st.markdown("---")
st.subheader("🔍 Prediction Result")

if prediction == 1:
    st.error(f"⚠️ **Likely to Churn** — Probability: `{prediction_prob:.2f}`")
else:
    st.success(f"✅ **Unlikely to Churn** — Probability: `{1 - prediction_prob:.2f}`")

# Show churn probability bar
st.markdown("#### 📈 Churn Probability")
st.progress(int(prediction_prob * 100))

# Footer
st.markdown("---")
st.caption("Model: K-Nearest Neighbors with GridSearchCV | Project by Arnob Ghosh")
