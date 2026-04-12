import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import matplotlib.pyplot as plt

# -------------------------------
# LOAD MODEL
# -------------------------------
MODEL_PATH = "rf_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found! Please keep rf_model.pkl in same folder.")
    st.stop()

model = joblib.load(MODEL_PATH)

# -------------------------------
# CREATE OUTPUT FOLDER
# -------------------------------
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(page_title="Cyber Threat Detection", layout="wide")
st.title("🛡️ AI Cybersecurity Threat Detection System")

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader("Upload Network Traffic CSV")

# -------------------------------
# MAIN LOGIC
# -------------------------------
if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Data Preview")
        st.write(df.head())

        # -------------------------------
        # CLEAN DATA
        # -------------------------------
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)

        # -------------------------------
        # PREPARE FEATURES
        # -------------------------------
        if "label" in df.columns:
            df["label"] = df["label"].apply(lambda x: 0 if x == "BENIGN" else 1)
            X = df.drop("label", axis=1)
        else:
            X = df

        st.write("✅ Feature shape:", X.shape)

        # -------------------------------
        # PREDICTION
        # -------------------------------
        predictions = model.predict(X)
        df["Prediction"] = predictions

        # -------------------------------
        # SAVE OUTPUT (VERY IMPORTANT)
        # -------------------------------
        st.write("💾 Saving file...")

        output_path = "outputs/predictions.csv"
        df.to_csv(output_path, index=False)

        if os.path.exists(output_path):
            st.success("✅ File saved successfully in outputs/predictions.csv")
        else:
            st.error("❌ File NOT saved")

        # -------------------------------
        # LABELS
        # -------------------------------
        df["Prediction_Label"] = df["Prediction"].map({
            0: "Normal ✅",
            1: "Attack 🚨"
        })

        # -------------------------------
        # ALERT SYSTEM
        # -------------------------------
        attack_count = int(sum(predictions))
        total = len(predictions)

        if attack_count > total * 0.3:
            alert = "HIGH 🚨"
        elif attack_count > total * 0.1:
            alert = "MEDIUM ⚠️"
        else:
            alert = "LOW ✅"

        # -------------------------------
        # RESULTS
        # -------------------------------
        st.subheader("📈 Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", total)
        col2.metric("Threats Detected", attack_count)
        col3.metric("Alert Level", alert)

        # Alert message
        if alert == "HIGH 🚨":
            st.error(f"🚨 ALERT LEVEL: {alert}")
        elif alert == "MEDIUM ⚠️":
            st.warning(f"⚠️ ALERT LEVEL: {alert}")
        else:
            st.success(f"✅ ALERT LEVEL: {alert}")

        # -------------------------------
        # SHOW PREDICTIONS
        # -------------------------------
        st.subheader("🔍 Predictions")
        st.write(df.head())

        # -------------------------------
        # BAR CHART
        # -------------------------------
        st.subheader("📊 Threat Distribution")
        st.bar_chart(df["Prediction"].value_counts())

        # -------------------------------
        # PIE CHART
        # -------------------------------
        st.subheader("🥧 Attack vs Normal")

        chart_data = df["Prediction"].value_counts()

        fig, ax = plt.subplots()
        ax.pie(chart_data, labels=["Normal", "Attack"], autopct="%1.1f%%")
        ax.set_title("Traffic Classification")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error: {e}")