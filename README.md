**IDS WITH ML**

A real-time Machine Learning based Intrusion Detection System that captures live network packets, 
classifies traffic as Normal or Suspicious, stores logs, and displays results in a SOC-style dashboard.

**Features**

- Real-time packet capture using Scapy
- ML-based traffic classification using Random Forest
- Flask-based live dashboard
- SQLite database logging
- Threat score calculation
- Suspicious IP tracking
- Alert system
- Blue-purple SOC-style UI

** Tech Stack**

- Python
- Flask
- Scapy
- SQLite
- Scikit-learn
- Joblib
- HTML, CSS, JavaScript
- Chart.js

**Project Structure**


IDS WITH ML/
├── app.py
├── capture.py
├── database.py
├── train_model.py
├── templates/
│   └── index.html
├── model/
│   └── ids_model.pkl
└── README.md


**How to Run**

Install dependencies--
pip install flask scapy scikit-learn pandas joblib

Create database--
python database.py

Train ML model--
python train_model.py

Start packet capture--
python capture.py

Start dashboard--
python app.py

Open in browser--
http://127.0.0.1:5000

**Project Description**

This project captures live packets using Scapy, extracts features such as packet length and protocol type, 
classifies traffic using a Random Forest model, stores logs in SQLite, and displays results in a real-time Flask dashboard.

**Author**
Dinesh Kumar
