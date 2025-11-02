
# 🛰️ HealthSat – A Remote Health Monitoring Communication Satellite

An IoT and satellite communication prototype that enables real-time health monitoring and emergency alerts in rural and remote areas.

## Overview

**HealthSat** is a satellite-based IoT system designed to provide reliable and continuous health monitoring for people living in remote and rural areas.  
It uses wearable sensors and long-range communication technologies to detect abnormal health conditions and send emergency alerts to nearby hospitals — even in regions without internet or mobile network coverage.

## Problem Statement

Access to healthcare is a major challenge in rural and remote areas due to limited hospitals and poor communication infrastructure.  
During medical emergencies, delays in reaching healthcare services can lead to preventable fatalities.  
**HealthSat** addresses this issue by using IoT devices and long-range communication to ensure that critical health data reaches hospitals in real time.

## Proposed Solution

The proposed solution integrates IoT hardware, low-power communication, and a monitoring dashboard to create a complete remote healthcare system.  
The system includes the following modules:

1. **ESP32 Microcontroller:** Performs data processing and communication control.  
2. **MAX30102 Pulse Oximeter Sensor:** Measures heart rate and SpO₂ levels continuously.  
3. **LoRa (SX1276) Transmitter & Receiver:** Ensures long-range, low-power communication between the patient unit and hospital base station, even without internet or mobile connectivity.  
4. **Streamlit-Based Hospital Dashboard:** Provides real-time visualization and alerts for abnormal readings, enabling healthcare professionals to act quickly.

When abnormal health parameters are detected, the ESP32 processes and encodes the data, transmits it via LoRa to the receiver at the hospital, and displays it on the dashboard. This ensures continuous monitoring and timely emergency response.

## Proposed System

The proposed system architecture is divided into multiple layers:

1. **Wearable Device Layer:** Collects real-time health parameters.  
2. **Communication Layer:** Transmits data via LoRa/Satellite networks.  
3. **Cloud Layer:** Stores data for access and analysis.  
4. **Hospital Dashboard:** Displays alerts and patient status to medical teams.  

### System Flow Diagram

![Proposed System Architecture](https://github.com/ThejaswiniS1/HealthSat_Remote_Health_Monitoring/blob/main/HealthSat_Proposed_System_Diagram.jpg)  
*Figure 1: Data flow and communication structure of the HealthSat proposed system.*

## Technologies Used

| Component | Technology / Module |
|------------|----------------------|
| Microcontroller | ESP32 (DevKit V1) |
| Sensor | MAX30102 Pulse Oximeter |
| Communication | LoRa SX1276, Satellite link |
| Programming | Micropython, C++ |
| Dashboard | Streamlit, Pandas, Matplotlib |
| Cloud Platform | Firebase / ThingsBoard |

## Code Overview

### Sender Code (ESP32)  
- Reads real-time heart rate and IR sensor values using the MAX30105 sensor.  
- Calculates BPM and sends data via LoRa at 866 MHz frequency.  
- Data format: `"BPM,IR_VALUE"`  

### Receiver Code (ESP32)  
- Receives transmitted data packets using LoRa and displays them on Serial Monitor.  
- Example output: Received packet: '78,56000' with RSSI -42

## Streamlit Dashboard

The **HealthSat Dashboard** is built using **Streamlit**, a lightweight Python framework for creating interactive web apps.  
It allows hospitals and healthcare professionals to view patient vitals in real time, including heart rate, SpO₂, and alerts.

### Features
- Real-time data visualization  
- Color-coded health alerts (Normal / Critical)  
- Historical plotting of heart rate  
- Works offline using sample data  

## Results and Discussion

The HealthSat system was tested to evaluate its accuracy, communication efficiency, and performance under real-time conditions.
The prototype demonstrated reliable health parameter monitoring and long-range data transmission using LoRa technology.

### System Performance Table

| **Parameter**               | **Test Condition**                | **Result/Observation**           | **Remarks**                       |
| --------------------------- | --------------------------------- | -------------------------------- | --------------------------------- |
| **Pulse Sensor Accuracy**   | Compared with commercial oximeter | 96% average accuracy             | Minor variation during motion     |
| **Data Transmission Delay** | Within 1.5 km LoRa range          | 2–3 seconds                      | Acceptable for real-time alerts   |
| **Communication Range**     | Open outdoor testing              | Up to 1.5 km                     | Stable signal without data loss   |
| **Power Consumption**       | Continuous operation (9V supply)  | 10+ hours                        | Low-power operation confirmed     |
| **Alert Trigger Response**  | Pulse <50 bpm or >120 bpm         | Instant alert on receiver screen | Successful emergency notification |

**Table 1:** System performance results of the *HealthSat* prototype.

### System Performance Results

![HealthSat System Performance Metrics](https://github.com/ThejaswiniS1/HealthSat_Remote_Health_Monitoring/blob/main/HealthSat_Performance_Results.jpg)
*Figure 2: Performance metrics of the HealthSat prototype system.*

These results confirm that the proposed system offers:

* High accuracy in physiological data monitoring
* Efficient and reliable long-range communication
* Low latency and power consumption
* Scalability for multi-node remote deployments

## Future Scope

* Integration of additional sensors (ECG, temperature, BP)
* Cloud-based AI analytics for anomaly detection
* Development of a mobile app for doctor–patient communication
* Integration with government rural healthcare networks



*🌍 By turning connectivity into care, **HealthSat** transforms how healthcare reaches people — making distance no longer a barrier to saving lives🫀.*

## Team Members
* **Tushar S** (1VA22IS109)
* **Tangirala Ruthu** (1VA22IS105)
* **Thejaswini S** (1VA22IS108)
* **Vaishnavi** (1VA22IS114)
  
**Department of Information Science and Engineering**,
**Sai Vidya Institute of Technology, Bengaluru**


