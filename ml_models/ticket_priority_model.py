import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib

# Load sample ticket data
df = pd.read_csv("../data/sample_tickets.csv")

# For demo purposes, ensure 'priority' exists
# If not, randomly assign for training
if 'priority' not in df.columns:
    import random
    df['priority'] = [random.choice(['low', 'medium', 'high']) for _ in range(len(df))]

# Features and target
X = df['description'] + " " + df['category']
y = df['priority']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline: TF-IDF vectorizer + Random Forest
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', RandomForestClassifier(n_estimators=200, random_state=42))
])

# Train model
pipeline.fit(X_train, y_train)

# Test accuracy
accuracy = pipeline.score(X_test, y_test)
print(f"Ticket Priority Prediction Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(pipeline, "../ml_models/ticket_priority_model.pkl")
print("Model saved as ticket_priority_model.pkl")
