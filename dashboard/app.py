import streamlit as st
import pandas as pd
from dashboard.components import plot_sentiment, plot_categories, show_metrics
import joblib

st.title("Customer Insights & Support Dashboard")

df = pd.read_csv("../data/sample_tickets.csv", parse_dates=["created_at"])

priority_model = joblib.load("ml_models/ticket_priority_model.pkl")
agent_model = joblib.load("ml_models/agent_assignment_model.pkl")
le_category = joblib.load("ml_models/le_category.pkl")
le_priority = joblib.load("ml_models/le_priority.pkl")
le_agent = joblib.load("ml_models/le_agent.pkl")

def predict_ticket(ticket):
    from dashboard.components import categorize_ticket
    category = categorize_ticket(ticket["description"])
    text = ticket["description"] + " " + category
    priority = priority_model.predict([text])[0]
    X_new = pd.DataFrame({
        "category": [le_category.transform([category])[0]],
        "priority": [le_priority.transform([priority])[0]]
    })
    agent_index = agent_model.predict(X_new)[0]
    assigned_agent = le_agent.inverse_transform([agent_index])[0]
    return priority, assigned_agent

df["predicted_priority"], df["assigned_agent"] = zip(*df.apply(predict_ticket, axis=1))

show_metrics(df)
plot_sentiment(df)
plot_categories(df)

st.subheader("ML Predictions")
st.dataframe(df[["subject", "category", "predicted_priority", "assigned_agent", "sentiment"]])
