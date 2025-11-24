# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="Salary Predictor", layout="centered")

st.title("💼 Salary Prediction App by Aniket")

st.write("Enter the details below to predict the employee's salary.")

MODEL_FILE = "Linear_model.pkl"

# ---------------------
# Load Model
# ---------------------
if not os.path.exists(MODEL_FILE):
    st.error(f"Model file '{MODEL_FILE}' not found in app directory.")
    st.stop()

try:
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Failed to load model file: {e}")
    st.stop()

# ---------------------
# Centered Input UI
# ---------------------
col = st.container()
with col:
    st.subheader("Enter Employee Details")

    exp = st.number_input("Experience (Years)", min_value=0.0, max_value=50.0, value=2.0)
    edu = st.selectbox("Education Level", [0, 1, 2])
    age = st.number_input("Age", min_value=18, max_value=70, value=25)

# Create DataFrame for prediction
input_df = pd.DataFrame([{
    "Experience": exp,
    "Education_Level": edu,
    "Age": age
}])

# ---------------------
# Prediction
# ---------------------
st.markdown("---")
if st.button("Predict Salary", use_container_width=True):
    try:
        pred = model.predict(input_df)[0]
        st.success(f"Estimated Salary: ₹ {pred:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
