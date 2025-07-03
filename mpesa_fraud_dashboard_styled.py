
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Page Config ----------------
st.set_page_config(page_title="MPesa Fraud Detection", layout="wide")

# ---------------- Custom Styling ----------------
def set_background():
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/6Iej2c3.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .block-container {
            background-color: rgba(255, 255, 255, 0.90);
            padding: 2rem;
            border-radius: 12px;
        }
        h1, h2, h3, .stMetric {
            color: #046c4e;
        }
        .stButton>button {
            background-color: #046c4e;
            color: white;
            border-radius: 8px;
        }
        .stSidebar {
            background-color: #eafaf3;
        }
        </style>
    """, unsafe_allow_html=True)

set_background()

# ---------------- App Login ----------------
def login():
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7d/M-Pesa_Logo.png", width=180)
    st.title("🔐 MPesa Fraud Detection Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid credentials. Try admin / 1234")

# ---------------- Main Dashboard ----------------
def dashboard():
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7d/M-Pesa_Logo.png", width=180)
    st.title("📊 MPesa Fraud Detection Dashboard")

    df = pd.read_csv("mpesa_fraud_predictions.csv")

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Hour'] = df['Timestamp'].dt.hour
    df['DayOfWeek'] = df['Timestamp'].dt.dayofweek

    st.sidebar.header("🔎 Filters")
    user_filter = st.sidebar.multiselect("Filter by User ID", options=df['UserID'].unique(), default=df['UserID'].unique())
    status_filter = st.sidebar.multiselect("Filter by Prediction", options=df['Predicted'].unique(), default=df['Predicted'].unique())

    filtered_df = df[(df['UserID'].isin(user_filter)) & (df['Predicted'].isin(status_filter))]

    st.subheader("📈 Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transactions", len(filtered_df))
    col2.metric("Detected Fraud", len(filtered_df[filtered_df['Predicted'] == 'Fraud']))
    col3.metric("Normal Transactions", len(filtered_df[filtered_df['Predicted'] == 'Normal']))

    st.subheader("📋 Transaction Table")
    st.dataframe(filtered_df, use_container_width=True)

    st.subheader("👤 Fraud Count by User")
    fraud_users = filtered_df[filtered_df['Predicted'] == 'Fraud']['UserID'].value_counts()
    st.bar_chart(fraud_users)

    st.subheader("💰 Amount Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df, x='Amount', hue='Predicted', kde=True, bins=30, ax=ax1)
    st.pyplot(fig1)

    st.subheader("🗺️ Fraud Heatmap (Hour vs Day)")
    fraud_only = filtered_df[filtered_df['Predicted'] == 'Fraud']
    heat_data = pd.crosstab(fraud_only['Hour'], fraud_only['DayOfWeek'])
    fig2, ax2 = plt.subplots()
    sns.heatmap(heat_data, cmap="YlGnBu", annot=True, fmt="d", ax=ax2)
    st.pyplot(fig2)

    st.download_button("⬇️ Download Filtered Data", data=filtered_df.to_csv(index=False), file_name="filtered_fraud_data.csv")

# ---------------- App Flow ----------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    dashboard()
