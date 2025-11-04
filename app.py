# 🩺 HealthSat - Remote Health Monitoring Dashboard
# Streamlit app for online demonstration and visualization
# Author: Team HealthSat (Thejaswini S, Tushar S, Tangirala Ruthu, Vaishnavi)

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
import altair as alt

# -----------------------------------------------
# 🎨 Page Configuration
# -----------------------------------------------
st.set_page_config(
    page_title="HealthSat Remote Health Monitoring",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------------------------
# 🩺 Title and Header
# -----------------------------------------------
st.title("🩺 HealthSat - Remote Health Monitoring Dashboard")
st.markdown("""
Welcome to **HealthSat**, an IoT-based remote health monitoring system designed for real-time 
tracking of vital parameters such as heart rate and SpO₂.  
This demo simulates sensor readings and displays them on a hospital dashboard for monitoring and alerting.
""")

# -----------------------------------------------
# ⚙️ Sidebar - Controls
# -----------------------------------------------
st.sidebar.header("🔧 Dashboard Controls")
refresh_rate = st.sidebar.slider("Data refresh rate (seconds):", 1, 10, 2)
alert_threshold_hr_low = st.sidebar.number_input("Low Heart Rate Threshold (BPM):", 40, 100, 50)
alert_threshold_hr_high = st.sidebar.number_input("High Heart Rate Threshold (BPM):", 100, 200, 120)
alert_threshold_spo2 = st.sidebar.number_input("SpO₂ Alert Threshold (%):", 80, 100, 92)

# -----------------------------------------------
# 📊 Simulated Live Data Function
# -----------------------------------------------
def generate_data():
    hr = np.random.randint(60, 110)
    spo2 = np.random.randint(90, 100)
    return hr, spo2

# Store data for graphing
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Heart Rate", "SpO₂"])

# -----------------------------------------------
# 🔄 Real-time Update Loop
# -----------------------------------------------
placeholder = st.empty()

for i in range(50):  # simulate 50 readings
    hr, spo2 = generate_data()
    current_time = datetime.now().strftime("%H:%M:%S")
    new_row = pd.DataFrame({"Time": [current_time], "Heart Rate": [hr], "SpO₂": [spo2]})
    st.session_state.data = pd.concat([st.session_state.data, new_row]).tail(30)  # keep last 30 readings

    # Determine alert condition
    if hr < alert_threshold_hr_low or hr > alert_threshold_hr_high or spo2 < alert_threshold_spo2:
        alert_status = "⚠️ **Critical**"
        alert_color = "red"
    else:
        alert_status = "✅ Normal"
        alert_color = "green"

    # -----------------------------------------------
    # 📋 Layout - 2 Columns
    # -----------------------------------------------
    with placeholder.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"### 🫀 Heart Rate: **{hr} BPM**")
            st.progress(min(hr / 200, 1.0))
            st.markdown(f"### 🌬️ SpO₂: **{spo2}%**")
            st.progress(min(spo2 / 100, 1.0))

        with col2:
            st.markdown(f"### 🧠 Current Status: <span style='color:{alert_color}'>{alert_status}</span>", unsafe_allow_html=True)
            st.markdown(f"Last updated: **{current_time}**")

        # Graphs
        st.markdown("### 📈 Real-Time Vital Graphs")
        chart_hr = (
            alt.Chart(st.session_state.data)
            .mark_line(color='crimson')
            .encode(x='Time', y='Heart Rate')
            .properties(height=200)
        )
        chart_spo2 = (
            alt.Chart(st.session_state.data)
            .mark_line(color='steelblue')
            .encode(x='Time', y='SpO₂')
            .properties(height=200)
        )
        st.altair_chart(chart_hr | chart_spo2, use_container_width=True)

        time.sleep(refresh_rate)

st.success("✅ Simulation complete - Dashboard ready for demo.")
