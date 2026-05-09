# Video Walkthrough Script: The "Silent Breach" Detection System

**Objective:** Demonstrate your ability to detect a SIM Swap attack and unauthorized HLR access using Splunk, showcasing your SOC analysis and threat hunting skills.

## Setup Before Recording
1. Ensure Splunk is running with your data ingested and the dashboard loaded.
2. Have the Threat Hunting Playbook open in another tab.
3. Ensure your screen recording software (e.g., OBS, Loom) is ready to capture your screen and webcam.

---

## Scene 1: Introduction (0:00 - 1:00)
- **Visual**: Webcam on, screen sharing the Splunk Dashboard.
- **Action**: Introduce yourself and the project.
- **Script**: "Hello, my name is Victor Dakang. Today I'll be demonstrating a SOC project I built called the 'Silent Breach' Detection System, designed specifically for the Telecom sector like MTN Nigeria or Verizon. The use case is detecting a SIM Swap attack that leads to account takeover, and hunting for unauthorized access to the Home Location Register, or HLR."

## Scene 2: The Dashboard & The Alert (1:00 - 2:30)
- **Visual**: Show the "Silent Breach" Splunk Dashboard.
- **Action**: Point to the "Anomalous Geolocation Login" and "SIM Swap Indicator" panels.
- **Script**: "Here is the Splunk dashboard I designed. As you can see, we've ingested Call Detail Records (CDRs) and authentication logs. An alert just fired on our dashboard indicating a potential SIM Swap. Notice the timeline: We see an IMSI (International Mobile Subscriber Identity) change for a specific subscriber, followed almost immediately by a login attempt to the self-care portal from a new, high-risk geolocation. It's geographically impossible for the user to travel that distance in such a short time."

## Scene 3: The Threat Hunt (2:30 - 4:00)
- **Visual**: Switch to the Splunk Search interface. Briefly flash the Threat Hunting Playbook in another tab.
- **Action**: Run the SPL query for HLR administrative access (copy from `splunk/queries/detection_queries.txt`).
- **Script**: "Following my CySA+ Threat Hunting Playbook, I'm pivoting to investigate if the attacker escalated privileges or manipulated backend systems. I'm running a query to look for unauthorized administrative access to the HLR around the time of the SIM swap. As you can see in these logs, there is an administrative action originating from a non-standard IP address modifying subscriber routing data, which confirms the 'Silent Breach' via SS7 manipulation."

## Scene 4: Conclusion & Remediation (4:00 - 5:00)
- **Visual**: Show a summary slide or keep it on the dashboard.
- **Action**: Summarize the findings and remediation steps.
- **Script**: "In a real-world scenario, the next steps according to my playbook would involve isolating the compromised admin account, reverting the unauthorized HLR changes, freezing the subscriber's account to prevent financial loss, and initiating an incident response ticket. This project demonstrates my ability to correlate disparate log sources, build actionable SIEM dashboards, and execute structured threat hunts in a complex telecom environment. Thank you for watching."
