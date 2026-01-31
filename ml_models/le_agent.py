import joblib
from sklearn.preprocessing import LabelEncoder

# Define agent names
agents = ["Alice", "Bob", "Charlie", "Diana"]

# Create and fit the encoder
le_agent = LabelEncoder()
le_agent.fit(agents)

# Save the encoder to ml_models/le_agent.pkl
joblib.dump(le_agent, "ml_models/le_agent.pkl")
print("le_agent.pkl saved successfully")
