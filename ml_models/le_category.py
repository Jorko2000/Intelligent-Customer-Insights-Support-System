import joblib
from sklearn.preprocessing import LabelEncoder

# Define the categories present in tickets
categories = ["technical", "billing", "general"]

# Create and fit the encoder
le_category = LabelEncoder()
le_category.fit(categories)

# Save the encoder to ml_models/le_category.pkl
joblib.dump(le_category, "ml_models/le_category.pkl")
print("le_category.pkl saved successfully")
