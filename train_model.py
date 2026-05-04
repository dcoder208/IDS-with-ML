import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# -----------------------------
# TRAINING DATA
# -----------------------------
# protocol:
# TCP = 6
# UDP = 17
# ICMP = 1
# OTHER = 0

data = [
    # Normal traffic
    [54, 6, 0],
    [60, 6, 0],
    [70, 6, 0],
    [120, 6, 0],
    [300, 6, 0],
    [500, 6, 0],
    [900, 6, 0],
    [1000, 6, 0],

    [100, 17, 0],
    [200, 17, 0],
    [400, 17, 0],
    [600, 17, 0],
    [800, 17, 0],

    # Suspicious traffic
    [40, 6, 1],
    [45, 6, 1],
    [50, 6, 1],
    [55, 6, 1],

    [1200, 6, 1],
    [1400, 6, 1],
    [1500, 6, 1],
    [2000, 6, 1],

    [64, 1, 1],
    [80, 1, 1],
    [100, 1, 1],
    [200, 1, 1],
    [500, 1, 1],

    [50, 0, 1],
    [1500, 0, 1],
]

df = pd.DataFrame(data, columns=["packet_length", "protocol_number", "label"])

X = df[["packet_length", "protocol_number"]]
y = df["label"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# -----------------------------
# MODEL TRAINING
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# MODEL TESTING
# -----------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, "model/ids_model.pkl")

print("\nML model saved successfully inside model/ids_model.pkl")
