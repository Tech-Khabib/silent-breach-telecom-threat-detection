import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Configuration
NUM_NORMAL_USERS = 50
TARGET_MSISDN = "+2348030000001"  # Target for SIM Swap (MTN Nigeria format)
START_TIME = datetime.now() - timedelta(days=2)

def generate_imsi():
    return "62120" + str(random.randint(1000000000, 9999999999)) # 62120 is MTN Nigeria PLMN

def generate_ip():
    return fake.ipv4()

def main():
    print("Generating synthetic telecom logs...")
    
    cdrs = []
    auth_logs = []
    hlr_logs = []
    
    users = []
    for _ in range(NUM_NORMAL_USERS):
        users.append({
            "msisdn": "+23480" + str(random.randint(10000000, 99999999)),
            "imsi": generate_imsi(),
            "location": "Lagos, Nigeria"
        })
        
    target_user = {
        "msisdn": TARGET_MSISDN,
        "imsi": generate_imsi(),
        "location": "Abuja, Nigeria"
    }
    users.append(target_user)

    current_time = START_TIME
    
    # Generate normal traffic for 1.5 days
    for _ in range(200):
        current_time += timedelta(minutes=random.randint(5, 30))
        user = random.choice(users)
        
        # Normal Auth Log
        auth_logs.append({
            "timestamp": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "MSISDN": user["msisdn"],
            "src_ip": generate_ip(),
            "City": user["location"].split(",")[0].strip(),
            "Country": "Nigeria",
            "action": "login_success"
        })

    # --- INJECT SIM SWAP ATTACK ---
    attack_time = current_time + timedelta(hours=1)
    new_imsi = generate_imsi()
    
    # 1. Unauthorized HLR Access (The Moat)
    hlr_logs.append({
        "timestamp": attack_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "Admin_ID": "admin_svc_09",
        "src_ip": "185.150.189.12", # Rogue IP
        "MSISDN": TARGET_MSISDN,
        "action": "MOD_SUB",
        "details": f"IMSI updated to {new_imsi}"
    })
    
    # 2. CDR Event: IMSI Change
    cdrs.append({
        "timestamp": (attack_time + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "EventCode": "IMSI_CHANGE",
        "MSISDN": TARGET_MSISDN,
        "old_IMSI": target_user["imsi"],
        "new_IMSI": new_imsi
    })
    
    # 3. Anomalous Login from Hacker (Geographically Impossible)
    hacker_time = attack_time + timedelta(minutes=15)
    auth_logs.append({
        "timestamp": hacker_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "MSISDN": TARGET_MSISDN,
        "src_ip": "45.22.19.122",
        "City": "Moscow",
        "Country": "Russia",
        "action": "login_success"
    })
    
    # Generate files
    with open('telecom_cdrs.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "EventCode", "MSISDN", "old_IMSI", "new_IMSI"])
        writer.writeheader()
        writer.writerows(cdrs)
        
    with open('auth_logs.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "MSISDN", "src_ip", "City", "Country", "action"])
        writer.writeheader()
        writer.writerows(auth_logs)
        
    with open('hlr_audit.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "Admin_ID", "src_ip", "MSISDN", "action", "details"])
        writer.writeheader()
        writer.writerows(hlr_logs)

    print("Successfully generated telecom_cdrs.csv, auth_logs.csv, and hlr_audit.csv")

if __name__ == "__main__":
    main()
