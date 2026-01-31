
import plotly.express as px
import pandas as pd
import streamlit as st

def plot_sentiment(df: pd.DataFrame):
    fig = px.histogram(df, x="sentiment", nbins=20, title="Ticket Sentiment Distribution")
    st.plotly_chart(fig)

def plot_categories(df: pd.DataFrame):
    fig = px.pie(df, names="category", title="Ticket Categories")
    st.plotly_chart(fig)

def show_metrics(df: pd.DataFrame):
    st.metric("Total Tickets", len(df))
    st.metric("Open Tickets", len(df[df["status"]=="open"]))
    st.metric("Closed Tickets", len(df[df["status"]=="closed"]))
