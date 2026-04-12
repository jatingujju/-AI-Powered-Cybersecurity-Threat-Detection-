import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("cicids2017.csv")

# Convert label (Binary)
df['label'] = df['label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

# Clean data
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Split features and target
X = df.drop("label", axis=1)
y = df["label"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "rf_model.pkl")

print("✅ Model trained and saved as rf_model.pkl")