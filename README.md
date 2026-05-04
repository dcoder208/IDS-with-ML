🛡️ IDS WITH ML (Intrusion Detection System

A real-time Machine Learning based Intrusion Detection System that captures live network packets, 
classifies traffic as Normal or Suspicious, stores logs, and displays results in a SOC-style dashboard.

🔥 Key Highlights
- ⚡ Real-time packet capture using **Scapy**
- 🤖 Machine Learning detection using **Random Forest**
- 📊 Live SOC dashboard using **Flask**
- 🧠 Dynamic threat scoring system
- 🚨 Real-time alert system
- 🌐 Top attacking IP identification
- 🎨 Modern blue-purple cyber security UI

📸 Dashboard Preview

> <img width="1882" height="887" alt="Screenshot 2026-05-04 175318" src="https://github.com/user-attachments/assets/867fa468-9ebf-44e0-8a44-bd64ed38dcc5" />

🛠️ Tech Stack

- Python
- Flask
- Scapy
- SQLite
- Scikit-learn
- Joblib
- HTML, CSS, JavaScript
- Chart.js

📂 Project Structure
<img width="202" height="452" alt="Screenshot 2026-05-04 175905" src="https://github.com/user-attachments/assets/d8cb0edc-7304-4c7a-becc-16bd071131d3" />

⚙️ How to Run
1️⃣ Install dependencies
pip install flask scapy scikit-learn pandas joblib

2️⃣ Create database
python database.py

3️⃣ Train ML model
python train_model.py

4️⃣ Start packet capture
python capture.py

5️⃣ Start dashboard
python app.py

🌐 Open in browser
http://127.0.0.1:5000

🧠 How it Works
-Captures live packets using Scapy <img width="1870" height="881" alt="Screenshot 2026-05-04 175448" src="https://github.com/user-attachments/assets/66ab5a35-0486-4396-a286-7262d9e9b8ae" />
-Extracts features (packet length, protocol)
-Classifies traffic using ML model <img width="1868" height="878" alt="Screenshot 2026-05-04 175420" src="https://github.com/user-attachments/assets/0b4b2215-518e-4e18-a14b-7664adfa7dd0" />
-Stores logs in SQLite
-Displays results in real-time dashboard

🎯 Use Case
This project simulates a Security Operations Center (SOC) environment and helps in detecting suspicious network activities in real time.

👨‍💻 Author 
Dinesh Kumar






