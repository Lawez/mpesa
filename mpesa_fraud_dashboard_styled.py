import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Fraud Detector", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to right, #e0f7fa, #e8f5e9);
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #046c4e;
    }
    .pitch-box {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-top: 1rem;
    }
    .button-style button {
        background-color: #046c4e;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.image("https://upload.wikimedia.org/wikipedia/commons/7/7d/M-Pesa_Logo.png", width=120)
st.title("Smart Fraud Detector")
st.markdown("### 🔍 Real-Time MPesa Fraud Analytics")

# ---------- About Section ----------
with st.container():
    st.markdown("""<div class="pitch-box">""", unsafe_allow_html=True)
    st.header("👋 Welcome to Our Developer Pitch")
    st.markdown("""
        We’re a passionate data science and engineering team based in Kenya 🇰🇪,
        building AI-powered solutions to tackle local and global financial fraud problems.
        
        This app showcases a **real-time fraud detection system** for MPesa transactions.

        💡 **Built with:** Python, Streamlit, Machine Learning, Pandas, Seaborn
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Features Section ----------
with st.container():
    st.markdown("""<div class="pitch-box">""", unsafe_allow_html=True)
    st.header("🚀 Key Features")
    st.markdown("""
    - 🧠 ML-based Fraud Classification  
    - 📊 Dynamic Visual Dashboards  
    - 🗺️ Heatmaps for Temporal Fraud Patterns  
    - 🔐 Login System with Secure Filtering  
    - ⬇️ Downloadable Reports
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- App Preview ----------
with st.container():
    st.markdown("""<div class="pitch-box">""", unsafe_allow_html=True)
    st.header("🖼️ App Preview")
    st.image("https://i.imgur.com/0v7Y9rh.png", caption="Interactive Fraud Dashboard")
    st.markdown("""
        This is a working model trained on realistic MPesa-style transaction data. 
        It can be expanded into APIs, enterprise integrations, or mobile alerts.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Call to Action ----------
with st.container():
    st.markdown("""<div class="pitch-box">""", unsafe_allow_html=True)
    st.header("📩 Let’s Work Together")
    st.markdown("""
    Are you a startup, fintech firm, or NGO needing data-driven insights?

    **Let’s connect and build together.**

    📧 Email: `iantulienge@gmail.com`  
    📍 Location: Nairobi, Kenya  
    """)
    st.button("Download CV / Portfolio", type="primary")
    st.markdown("</div>", unsafe_allow_html=True)
