# **FraudIQ – ML Risk Analysis Tool**

FraudIQ is a machine learning-powered tool for assessing the risk of credit card transactions. Built as a full-stack prototype, it allows users to interact with a logistic regression model in real time and generate transaction risk reports.

![FraudIQ Dashboard](https://github.com/user-attachments/assets/53ddb62e-ad69-4334-8db1-4c7dbbdc63ac)

---

## 🚀 **Key Features**

- **Logistic Regression Model**  
  Trained on 284,807 credit card transactions with a validation accuracy of **97.5%**.

- **Risk Scoring System**  
  Calculates a fraud risk score (0–100) and classifies transactions into **Low**, **Medium**, or **High Risk**.

- **Real-Time Analysis**  
  Users input transaction amount and time, and receive immediate risk evaluations.

- **Risk Summary Report**  
  Generates a downloadable PDF summarizing the number of transactions, risk distribution, average score, and max score.

---

## 🧑‍💻 **Tech Stack**

- **Frontend**: React.js  
  Interactive dashboard with chart visualizations using Recharts.

- **Backend**: Flask  
  REST API serving real-time predictions and generating risk reports.

- **Machine Learning**:  
  Logistic Regression using scikit-learn, with **SMOTE** to address class imbalance.

---

## 📊 **How It Works**

1. **User Input**  
   Enter transaction amount and time through the React dashboard.

2. **Prediction**  
   Backend model returns a risk score and level based on the trained logistic regression model.

3. **Visualization**  
   View results through a dynamic chart and summary card.

4. **Report Generation**  
   Instantly generate a downloadable PDF with all relevant transaction risk data.

---

## 🖥️ **Installation & Setup**

```bash
# Clone the repository
git clone https://github.com/your-username/FraudIQ.git
cd FraudIQ

# Install backend dependencies
pip install -r requirements.txt

# Run the backend
python app.py

# Navigate to frontend directory
cd client

# Install frontend dependencies
npm install

# Start the React frontend
npm start
