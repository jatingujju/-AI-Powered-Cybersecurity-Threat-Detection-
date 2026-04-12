# -AI-Powered-Cybersecurity-Threat-Detection-
# 🛡️ AI-Powered Cybersecurity Threat Detection System

## 📌 Project Overview
This project presents an AI-powered cybersecurity threat detection system that analyzes network traffic data and classifies it as either normal or malicious activity.

The system is built using machine learning techniques and simulates a real-world Security Operations Center (SOC) environment where cyber threats are detected and monitored.

---

## 🚨 Problem Statement
Traditional rule-based cybersecurity systems fail to detect modern and evolving cyber threats. Organizations need intelligent systems that can automatically identify suspicious activities in network traffic.

This project addresses this problem using machine learning to detect cyber threats efficiently.

---

## 🎯 Objectives
- Detect cyber attacks from network traffic data  
- Classify traffic as **Normal** or **Attack**  
- Build an interactive dashboard for visualization  
- Generate alert levels based on detected threats  
- Simulate real-world cybersecurity monitoring  

---

## 🧠 Industry Relevance
This system can be applied in:
- Banks for fraud detection  
- IT companies for network monitoring  
- Product-based companies for intrusion detection  
- SOC teams for real-time threat analysis  

---

## 📊 Dataset
- Dataset: **CICIDS2017**
- Contains realistic network traffic data
- Includes multiple attack types such as:
  - DDoS
  - Brute Force
  - Botnet
  - Infiltration

---

## ⚙️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib  
- Joblib  
- Flask (optional for API)  

---

## 🏗️ Project Architecture
1. Data Collection (CICIDS dataset)  
2. Data Preprocessing & Cleaning  
3. Feature Engineering  
4. Model Training (Random Forest)  
5. Prediction System  
6. Alert Generation  
7. Visualization Dashboard  

---

## 🤖 Machine Learning Model
- Algorithm: **Random Forest Classifier**
- Type: Supervised Learning  
- Output:
  - 0 → Normal  
  - 1 → Attack  

---

## 📈 Features
- Upload network traffic CSV file  
- Automatic preprocessing  
- Real-time prediction  
- Alert system:
  - HIGH 🚨  
  - MEDIUM ⚠️  
  - LOW ✅  
- Graph visualization (bar & pie charts)  
- User-friendly dashboard  

---

## 🖥️ How to Run the Project

### Step 1: Clone Repository
```bash
git clone https://github.com/jatingujju/AI-Cybersecurity-Threat-Detection.git

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Train Model (Optional)
python train_model.py

Step 4: Run Dashboard
python -m streamlit run app.py

Step 5: Open in Browser
http://localhost:8501
