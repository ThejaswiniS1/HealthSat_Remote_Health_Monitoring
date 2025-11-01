# HealthSat_Remote_Health_Monitoring
An IoT and satellite communication prototype that enables real-time health monitoring and emergency alerts in rural areas.

### 🛰️ HealthSat – A Remote Health Monitoring Communication Satellite

### Overview:

HealthSat is a satellite-based IoT system designed to provide reliable and continuous health monitoring for people living in remote and rural areas.  
It uses wearable sensors and long-range communication technologies to detect abnormal health conditions and send emergency alerts to nearby hospitals — even in regions without internet or mobile network coverage.

### Problem Statement
Access to healthcare is a major challenge in rural and remote areas due to limited hospitals and poor communication infrastructure.  
During medical emergencies, delays in reaching healthcare services can lead to preventable fatalities.  
**HealthSat** addresses this issue by using IoT devices and satellite communication to ensure that critical health data reaches hospitals in real time.

### Proposed Solution
The proposed system integrates:
- ESP32 Microcontroller** for data processing  
- MAX30102 Pulse Oximeter Sensor for real-time heart rate and SpO₂ monitoring  
- LoRa (SX1276)** for long-range, low-power data transmission  
- Web Dashboard (Streamlit, Python) for hospital monitoring  

When an abnormal pulse or oxygen level is detected, an alert message with GPS coordinates is transmitted via LoRa or satellite to the nearest hospital, enabling quick medical intervention.

### System Architecture
1. Wearable Device Layer: Collects real-time health parameters.  
2. Communication Layer: Transmits data via LoRa/Satellite networks.  
3. Cloud Layer: Stores data for access and analysis.  
4. Hospital Dashboard: Displays alerts and patient status to medical teams.  

### Technologies Used
| Component | Technology / Module |
|------------|----------------------|
| Microcontroller | ESP32 (DevKit V1) |
| Sensor | MAX30102 Pulse Oximeter |
| Communication | LoRa SX1276, Satellite link |
| Programming | Micropython, C++ |
| Dashboard | Streamlit, Pandas, Matplotlib |
| Cloud Platform | Firebase / ThingsBoard |

### Code Overview

Sender Code (ESP32)
- File: `/code/sender/sender_esp32
- Reads real-time heart rate and IR sensor values using the MAX30105 sensor.
- Calculates BPM and sends data via LoRa at 866 MHz frequency.
- Data format: `"BPM,IR_VALUE"`

Receiver Code (ESP32)
- File: `/code/receiver/receiver_esp32`
- Receives transmitted data packets using LoRa and displays them on Serial Monitor.
- Example output-> Received packet: '78,56000' with RSSI -42


### Streamlit Dashboard

The HealthSat Dashboard is built using Streamlit, a lightweight Python framework for creating interactive web apps.  
It allows hospitals and healthcare professionals to view patient vitals in real-time, including heart rate, SpO₂, and alerts.

Features
- Real-time data visualization  
- Color-coded health alerts (Normal / Critical)  
- Historical plotting of heart rate  
- Works offline using sample data  

How to Run
```bash
cd dashboard_streamlit
pip install -r requirements.txt
streamlit run app.py



