# Splunk Enterprise Local Setup Guide

If you do not currently have Splunk Enterprise installed, follow this guide to set it up locally for the "Silent Breach" project. 

There are two primary ways to set up Splunk locally: via Docker (recommended if you have Docker Desktop) or via a direct OS installation.

## Option A: Splunk via Docker (Recommended, Fastest)

This is the cleanest and fastest way to get Splunk running without altering your host system.

1. **Prerequisite**: Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
2. Open your terminal (PowerShell, Command Prompt, or Terminal).
3. Run the following command to pull and start the Splunk Enterprise image:
   ```bash
   docker run -d -p 8000:8000 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=KhabibPassword123!" --name splunk splunk/splunk:latest
   ```
4. Wait about 1-2 minutes for the container to initialize.
5. Open your web browser and navigate to `http://localhost:8000`.
6. Log in using:
   - **Username**: `admin`
   - **Password**: `KhabibPassword123!`

## Option B: Direct OS Installation

If you prefer not to use Docker, you can install the Splunk Free Trial directly on your machine.

1. Go to the [Splunk Free Trials website](https://www.splunk.com/en_us/download/splunk-enterprise.html).
2. Create a free account or log in.
3. Download the installer for your Operating System (Windows, macOS, or Linux).
4. Run the installer and follow the on-screen instructions. 
   - *Important*: Remember the administrator username and password you set during the installation.
5. Once installed, it will automatically launch your browser to `http://localhost:8000`.
6. Log in with the credentials you just created.

---

## Ingesting the Datasets into Splunk

Once you are logged into Splunk (via Option A or Option B), you need to ingest the CSV files we generated (`telecom_cdrs.csv`, `auth_logs.csv`, `hlr_audit.csv`).

1. **Create the Index**:
   - Go to **Settings** (top right) -> **Indexes**.
   - Click **New Index**.
   - Set the Index Name to `telecom` and click **Save**.

2. **Upload the Data**:
   - Click on **Settings** -> **Add Data**.
   - Click **Upload** (Upload files from my computer).
   - Select `telecom_cdrs.csv`.
   - Click **Next**.
   - Splunk will parse the CSV. On the Set Sourcetype page, click **Save As** and name the sourcetype `telecom_cdrs`. Click **Next**.
   - On the Input Settings page, change the Index to `telecom`. Click **Review** -> **Submit**.
   
3. **Repeat for the other two files**:
   - Upload `auth_logs.csv`. Save the sourcetype as `auth_logs` and put it in the `telecom` index.
   - Upload `hlr_audit.csv`. Save the sourcetype as `hlr_audit` and put it in the `telecom` index.

---

## Verifying the Data

To ensure the data is in your system:
1. Click on **Search & Reporting** on the left menu.
2. In the search bar, type: `index="telecom"`
3. Make sure the time picker (right next to the search button) is set to **All time** (since our mock data was generated for the past 2 days).
4. Hit search. You should see thousands of events populated!

Once you complete this, you are officially done with Phase 1 and ready to move to Phase 2 (Dashboards and Alerts)!
