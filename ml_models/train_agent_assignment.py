import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample agent data
agents = ["Alice", "Bob", "Charlie", "Diana"]

# Simulate historical tickets
data = {
    "category": ["technical", "billing", "technical", "general", "billing", "technical"]*10,
    "priority": ["high", "medium", "low", "medium", "high", "low"]*10,
    "assigned_agent": ["Alice", "Bob", "Charlie", "Diana", "Bob", "Alice"]*10
}
df = pd.DataFrame(data)

# Encode categorical features
le_category = LabelEncoder()
le_priority = LabelEncoder()
le_agent = LabelEncoder()

X = pd.DataFrame({
    "category": le_category.fit_transform(df["category"]),
    "priority": le_priority.fit_transform(df["priority"])
})
y = le_agent.fit_transform(df["assigned_agent"])

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Save the model and encoders
joblib.dump(clf, "../ml_models/agent_assignment_model.pkl")
joblib.dump(le_category, "../ml_models/le_category.pkl")
joblib.dump(le_priority, "../ml_models/le_priority.pkl")
joblib.dump(le_agent, "../ml_models/le_agent.pkl")

print("Agent assignment model and encoders saved successfully")
