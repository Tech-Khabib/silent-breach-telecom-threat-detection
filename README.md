# The "Silent Breach" Detection System

## Overview
This repository contains a SOC portfolio project designed for the Telecommunications & ISP sector (e.g., MTN Nigeria, Verizon). The project focuses on detecting "SIM Swap" fraud and Signaling System 7 (SS7) attacks. 

The core of the detection mechanism relies on correlating telecom-specific Call Detail Records (CDR) with suspicious authentication and geolocation logs to identify Account Takeover (ATO) attempts and unauthorized administrative access to the Home Location Register (HLR).

## Project Architecture
- **Data Generation**: A Python script generates realistic, synthetic telecom logs simulating a SIM Swap attack.
- **SIEM (Splunk)**: Ingestion of the mock data into Splunk to visualize, correlate, and trigger alerts on anomalous behavior.
- **Threat Hunting Playbook**: A CySA+ aligned playbook detailing steps to identify unauthorized HLR access.

## Repository Structure
- `/data_generation/`: Python script to generate mock CDR and authentication logs.
- `/playbooks/`: CySA+ aligned Threat Hunting playbook for HLR.
- `/splunk/`: Splunk dashboard XML and SPL queries for the detection system.
- `/demo/`: A step-by-step video walkthrough script.

## Quick Start
1. **Prerequisites:** Python 3.x, Splunk Enterprise (Free or Trial).
2. **Install Python dependencies:** `pip install -r requirements.txt`
3. **Generate Mock Data:** Run the python script in `/data_generation/generate_telecom_logs.py`. This will create `telecom_cdrs.csv` and `auth_logs.csv`.
4. **Setup Splunk:** Ingest the generated CSV files into your Splunk instance. Make sure to set the sourcetype properly and extract JSON fields if necessary.
5. **Import Dashboard:** Navigate to Splunk Dashboards, create a new dashboard, click "Source", and paste the XML from `/splunk/dashboards/silent_breach_dashboard.xml`.
