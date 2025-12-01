 🔥 Smart Firewall Rule Recommendation System  
Machine Learning–Driven Firewall Rule Generator with Streamlit UI

📌 Overview

The Smart Firewall Rule Recommendation System is a machine-learning–based application designed to analyze network logs and automatically **recommend firewall rules** that help block or allow traffic based on learned patterns.

This project supports:
- Uploading network log files (CSV format)
- Cleaning & preprocessing network traffic data
- Training a Decision Tree Classifier
- Predicting ALLOW/BLOCK decisions based on port behavior
- Automatically generating structured firewall rule objects
- Downloading rules as JSON
- Saving user feedback for continuous improvement
- A fully interactive **Streamlit UI**

This project was developed as part of an **Applied Cybersecurity / Software Engineering Project**.

---

 🚀 Features

🔍 1. Log Ingestion & Preprocessing
- Reads CSV network logs  
- Drops missing values  
- Generates labels (`ALLOW` → 1, `BLOCK` → 0)

🤖 2. Machine Learning Engine
- Decision Tree classifier (scikit-learn)  
- Trained on port-based traffic classification  
- Saves and loads model using `joblib`

🛡️ 3. Intelligent Rule Generation
Given a port number, the system:
- Predicts whether traffic should be **allowed** or **blocked**
- Generates a structured firewall rule object containing:
  - Source IP
  - Destination IP
  - Protocol
  - Port
  - Action (ALLOW/BLOCK)
  - Recommendation description

🖥️ 4. Streamlit Frontend
The UI supports:
- Upload logs  
- Preview data  
- Train model  
- Enter port number  
- Generate & download rule  
- Submit feedback  

📝 5. Feedback System
- User comments stored in `outputs/feedback.json`  
- Enables future model refinement

---

🏗️ Project Structure
smart-firewall-project/
├─ data/
│ └─ network_logs.csv
├─ models/
│ └─ decision_tree.pkl
├─ outputs/
│ └─ feedback.json
├─ src/
│ ├─ preprocess.py
│ ├─ train_model.py
│ ├─ recommend_rules.py
│ └─ feedback.py
├─ ui/
│ └─ app.py
├─ test_cases/
├─ requirements.txt
├─ README.md
└─ .gitignore


---

⚙️ Installation & Setup 

1️⃣ Clone the Repository 
bash 
git clone https://github.com/Kunj0512/smart-firewall-project.git
cd smart-firewall-project

3️⃣ Install Dependencies
bash
pip install -r requirements.txt

▶️ Running the Application
bash
Start the Streamlit Application
streamlit run ui/app.py

Using the App

Upload a network_logs.csv file

Preview logs

Train the model

Enter a port number

Generate the recommended firewall rule

Download rule as JSON

Provide feedback (optional)

📘 Example Rule Output
JSON
{
  "source": "any",
  "destination": "any",
  "protocol": "TCP",
  "port": 22,
  "action": "BLOCK",
  "description": "Traffic on port 22 should be blocked based on model prediction."
}

🧪 Testing (Optional)

If tests are added in future:

pytest

🎥 Video Walkthrough (Add Link)

A full project walkthrough video will be added here:

https://myharrisburgu-my.sharepoint.com/:v:/g/personal/ktrivedi1_my_harrisburgu_edu/Ecsb67i1biVPnwgfZt8cbF8B8hdN8Uj9VKFZAX06mgRILw?e=zayZTe&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D

🧠 Future Improvements

Add multi-feature ML training (source IP, protocol, packet size)

Upgrade ML model (Random Forest, XGBoost)

Add analytics dashboard

Integrate with pfSense, iptables, Azure NSG APIs

Add role-based access control (RBAC)

📄 License

This project is licensed under the MIT License.
You may use, modify, and distribute this project with attribution.

👤 Author

Kunj Trivedi
GitHub: @Kunj0512

Project: Smart Firewall Rule Recommendation System (2024–2025)