from scapy.all import sniff, IP, TCP, UDP, ICMP
import sqlite3
from datetime import datetime
import joblib
import os

# -----------------------------
# LOAD ML MODEL
# -----------------------------
MODEL_PATH = "model/ids_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("ML model loaded successfully.")
else:
    model = None
    print("ML model not found. Run train_model.py first.")


# -----------------------------
# SAVE PACKET TO DATABASE
# -----------------------------
def save_packet(source_ip, destination_ip, protocol, packet_length, status):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO logs (timestamp, source_ip, destination_ip, protocol, packet_length, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        source_ip,
        destination_ip,
        protocol,
        packet_length,
        status
    ))

    conn.commit()
    conn.close()


# -----------------------------
# GET PROTOCOL
# -----------------------------
def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP", 6
    elif packet.haslayer(UDP):
        return "UDP", 17
    elif packet.haslayer(ICMP):
        return "ICMP", 1
    else:
        return "OTHER", 0


# -----------------------------
# ML PREDICTION WITH REASON
# -----------------------------
def predict_status(packet_length, protocol_number):
    if model is None:
        return "Unknown", "Model not loaded"

    features = [[packet_length, protocol_number]]
    prediction = model.predict(features)[0]

    if prediction == 1:
        if protocol_number == 1:
            return "Suspicious", "ICMP anomaly detected"
        elif packet_length < 60:
            return "Suspicious", "Small packet anomaly detected"
        elif packet_length > 1200:
            return "Suspicious", "Large packet anomaly detected"
        elif protocol_number == 0:
            return "Suspicious", "Unknown protocol anomaly"
        else:
            return "Suspicious", "ML anomaly detected"
    else:
        return "Normal", "Legitimate traffic"


# -----------------------------
# PACKET CAPTURE FUNCTION
# -----------------------------
def detect_packet(packet):
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        protocol, protocol_number = get_protocol(packet)
        packet_length = len(packet)

        status, reason = predict_status(packet_length, protocol_number)

        save_packet(
            source_ip,
            destination_ip,
            protocol,
            packet_length,
            status
        )

        print(
            f"[+] {source_ip} -> {destination_ip} | "
            f"{protocol} | {packet_length} bytes | "
            f"ML Prediction: {status} | Reason: {reason}"
        )


print("Starting ML-based IDS packet capture...")
print("Press CTRL + C to stop.")

sniff(prn=detect_packet, store=False)