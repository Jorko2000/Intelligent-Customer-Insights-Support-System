import joblib
from sklearn.preprocessing import LabelEncoder

# Define priority levels
priorities = ["high", "medium", "low"]

# Create and fit the encoder
le_priority = LabelEncoder()
le_priority.fit(priorities)

# Save the encoder to ml_models/le_priority.pkl
joblib.dump(le_priority, "ml_models/le_priority.pkl")
print("le_priority.pkl saved successfully")
