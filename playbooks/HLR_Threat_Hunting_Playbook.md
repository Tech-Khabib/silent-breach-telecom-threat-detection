# Threat Hunting Playbook: HLR Unauthorized Access & SIM Swap

**Alignment:** CompTIA CySA+ (CS0-003) Threat Hunting & Incident Response Methodologies
**Target Environment:** Telecom Core Network (HLR/HSS), ISP Infrastructure

## 1. Preparation & Hypothesis
**Hypothesis:** An attacker has gained unauthorized access to the Home Location Register (HLR) via compromised administrative credentials or SS7 vulnerabilities to facilitate a SIM Swap attack (changing a victim's IMSI mapping).
**Data Sources Required:**
- Call Detail Records (CDRs)
- HLR Administrative Audit Logs
- Subscriber Self-Care Portal Authentication Logs
- VPN/Remote Access Logs

## 2. Investigation Triggers (Indicators of Compromise)
- Sudden change in IMSI associated with an active MSISDN (Phone Number).
- Geographically impossible logins (e.g., login from Lagos, Nigeria, followed by a login from Moscow, Russia within 1 hour).
- HLR administrative actions (e.g., `MOD_SUB`, `UPDATE_LOCATION`) occurring outside standard maintenance windows or from non-standard IP ranges.

## 3. Hunt Execution Steps
### Step 3.1: Correlate IMSI Changes with Geolocation Anomalies
*Goal: Identify potential account takeovers resulting from unauthorized SIM Swaps.*
- Search Splunk for `EventCode=IMSI_CHANGE`.
- Correlate the affected `MSISDN` with recent authentication logs (`sourcetype=auth_logs`).
- Calculate the distance and time between the last known good login and the login immediately following the IMSI change.
- **SPL Query:** (Refer to `splunk/queries/detection_queries.txt` - Query 1)

### Step 3.2: Investigate HLR Administrative Access
*Goal: Determine if the IMSI change was authorized or anomalous.*
- Search HLR audit logs (`sourcetype=hlr_audit`) for the affected `MSISDN` around the time of the IMSI change.
- Look for administrative commands like `MOD_SUB` (Modify Subscriber).
- Check the `Source_IP` and `Admin_ID` associated with the command.
- **SPL Query:** (Refer to `splunk/queries/detection_queries.txt` - Query 2)

### Step 3.3: Privilege Escalation and Lateral Movement Check
*Goal: Identify how the attacker accessed the HLR.*
- If an anomalous `Admin_ID` or `Source_IP` is found, pivot to VPN or active directory logs.
- Search for multiple failed logins, unusual access times, or concurrent sessions for that Admin_ID.

## 4. Remediation & Eradication
- **Isolate:** Disable the compromised Admin_ID and block the anomalous Source IP at the firewall.
- **Revert:** Revert the subscriber's HLR profile to the legitimate IMSI.
- **Protect:** Temporarily freeze the subscriber's self-care portal access and notify them via alternate out-of-band methods.
- **Review:** Audit SS7 perimeter firewalls (STP) for unauthorized signaling messages (e.g., unexpected `SendRoutingInfo`).
