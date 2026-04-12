from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# --- Clean data ---
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# --- Convert label (Binary Classification) ---
df['label'] = df['label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

# --- Split data ---
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Train model ---
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
