import streamlit as st
import pandas as pd
import time

st.title("🩺 HealthSat - Remote Health Monitoring Dashboard")

st.write("Monitoring real-time health data from ESP32 + LoRa system")

# Placeholder for dynamic data
placeholder = st.empty()

# Example live data simulation
for i in range(10):
    data = {
        "Heart Rate (BPM)": [75 + i % 5],
        "IR Value": [56000 + i * 50],
        "Status": ["Normal" if i % 7 != 0 else "Alert 🚨"]
    }
    df = pd.DataFrame(data)
    with placeholder.container():
        st.subheader("Live Health Data")
        st.table(df)
        st.progress((i + 1) * 10)
    time.sleep(1)
