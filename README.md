# Silent Breach Detection System
### Telecom Detection Engineering for SIM Swap Fraud & SS7 Attack Detection using Splunk

## Executive Summary
Telecommunications providers process millions of subscriber transactions every day. While these operations enable seamless communication, they also present attractive targets for attackers seeking to hijack customer identities, intercept communications, and compromise critical network infrastructure.

Among the most damaging threats are SIM Swap Fraud and Signaling System No. 7 (SS7) attacks, both of which can lead to account takeover, financial fraud, unauthorized subscriber provisioning, and large-scale customer compromise.

This project demonstrates how a Security Operations Center (SOC) can detect these attacks by correlating telecom-specific Call Detail Records (CDRs), authentication events, administrative activities, and geolocation anomalies within Splunk Enterprise.

Rather than relying on isolated alerts, the solution combines multiple telemetry sources into a unified detection workflow that improves analyst visibility, accelerates threat detection, and supports evidence-based incident response.
## Business Problem
Telecommunications organizations face increasingly sophisticated attacks targeting subscriber identity management systems.

Traditional monitoring solutions often detect only isolated events, making it difficult for analysts to determine whether suspicious activities represent legitimate subscriber behavior or coordinated attacks.

Examples include:

- SIM Swap fraud
- Unauthorized Home Location Register (HLR) access
- Rogue administrator activity
- Subscriber identity manipulation
- SS7 signaling abuse
- Account Takeover (ATO)

Without effective event correlation, these attacks can remain undetected until customer accounts have already been compromised.
## Solution Architecture
<img width="645" height="471" alt="image" src="https://github.com/user-attachments/assets/ab877b5b-094c-467b-ace8-0898aa2640d1" />

## Project Preview
<img width="1901" height="893" alt="Screenshot 2026-06-27 202557" src="https://github.com/user-attachments/assets/430f4bb4-3bab-4809-ab2f-faf3e79291e3" />
<img width="1912" height="896" alt="Screenshot 2026-06-27 202618" src="https://github.com/user-attachments/assets/0d4bf3c3-c0f9-4874-9707-fe3fad34dd20" />
<img width="1898" height="850" alt="Screenshot 2026-06-27 202635" src="https://github.com/user-attachments/assets/9f90b55e-eeac-4a11-bc3b-3e482297a069" />
<img width="1895" height="442" alt="Screenshot 2026-06-27 202651" src="https://github.com/user-attachments/assets/f3bd553c-5c90-4a03-a43a-2df81df8f5f0" />

## Detection Objectives
The primary objectives of this project are to:

- Detect SIM Swap fraud.
- Identify unauthorized HLR administrative activity.
- Correlate telecom events across multiple log sources.
- Detect suspicious authentication behavior.
- Identify impossible travel and geolocation anomalies.
- Reduce investigation time through centralized visualization.
- Demonstrate telecom-focused detection engineering using Splunk.
## Detection Workflow

### 1. Telecom Log Generation

A Python-based simulation generates realistic telecom security events, including:

- Call Detail Records (CDRs)
- Authentication logs
- Administrative HLR events
- Subscriber identity changes
- Geolocation information

The generated dataset provides a controlled environment for detection engineering and SOC investigations.

### 2. Data Ingestion

Generated logs are ingested into Splunk Enterprise for indexing and normalization.

Example data sources include:

- Subscriber activity
- Authentication logs
- Administrative events
- Call metadata
- Network activity
### 3. Event Correlation

Splunk Search Processing Language (SPL) correlates multiple event sources to identify suspicious activity that would otherwise appear unrelated.

Correlation scenarios include:

- SIM replacement followed by abnormal authentication.
- HLR administrator access outside approved maintenance windows.
- Subscriber authentication from geographically distant locations.
- Multiple authentication failures preceding SIM activation.
- Privileged account activity targeting subscriber records.
### 4. Threat Detection

The dashboard enables analysts to investigate indicators of compromise associated with:

- SIM Swap Fraud
- Account Takeover (ATO)
- Insider Threat
- Privileged Account Abuse
- SS7-related activity
- Unauthorized Subscriber Provisioning
### 5. Threat Hunting

A CySA+-aligned threat hunting playbook guides analysts through the investigation process by documenting:

- Initial triage
- Evidence collection
- Event correlation
- Validation procedures
- Escalation criteria
- Recommended response actions

  ## Technical Highlights
  This project demonstrates practical implementation of:

- Telecom security monitoring
- Detection engineering
- Splunk Dashboard Studio
- Splunk Search Processing Language (SPL)
- Security event correlation
- Python log simulation
- Threat hunting
- SIEM engineering
- Geolocation anomaly detection
- Administrative activity monitoring

## Skills Demonstrated

This repository demonstrates practical experience in:

- Detection Engineering
- Security Operations Center (SOC)
- Threat Hunting
- Splunk Administration
- SIEM Engineering
- Telecom Security Monitoring
- Event Correlation
- Python Automation
- Dashboard Engineering
- Cyber Threat Detection
- Security Reporting
- Incident Investigation
## Business Value

The solution helps telecommunications organizations by:

- Improving visibility into subscriber-focused attacks.
- Accelerating SIM Swap investigations.
- Detecting privileged administrative abuse.
- Reducing analyst investigation time.
- Supporting evidence-based incident response.
- Improving SOC operational efficiency.
- Demonstrating telecom-specific detection capabilities.

## Getting Started
### Prerequisites
- Python 3.x
- Splunk Enterprise (Free or Trial Edition)
### Installation

Install the required dependencies:

pip install -r requirements.txt

Generate synthetic telecom logs:

python data_generation/generate_telecom_logs.py

This generates:

- telecom_cdrs.csv
- auth_logs.csv

Import the generated datasets into Splunk Enterprise.

Create the appropriate indexes or sourcetypes as required.

Import the dashboard configuration from the splunk/ directory and begin investigating simulated telecom attack scenarios.

## Project Limitations

This repository is intended for educational and portfolio purposes.

Current limitations include:

- Synthetic datasets only
- No live SS7 signaling integration
- No automated response capability
- No SOAR integration
- Limited to simulated telecom environments
## Future Enhancements

Potential future improvements include:

- Real-time streaming log ingestion
- SOAR integration
- UEBA-based anomaly detection
- Risk scoring for subscribers
- Threat intelligence enrichment
- Machine learning-based fraud detection
- Executive KPI dashboard
- Automated incident response workflows
## Key Takeaways

The Silent Breach Detection System demonstrates how industry-specific detection engineering can improve visibility into sophisticated telecommunications attacks by combining synthetic log generation, event correlation, dashboard engineering, and structured threat hunting.

Rather than focusing solely on alert generation, the project emphasizes investigative context, attacker behavior, and operational decision-making, core capabilities expected within modern telecommunications Security Operations Centers.
## Author

### Dakang Victor Ladat

Cyber Defense Analyst | Detection Engineering | Security Operations (SOC) | Threat Hunting | Incident Response | Digital Forensics | SIEM Engineering | Governance, Risk & Compliance (GRC)
