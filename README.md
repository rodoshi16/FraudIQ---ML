# **FraudIQ – ML Risk Analysis Tool**

FraudIQ is a machine learning-powered fraud detection prototype designed to help financial institutions assess the risk of credit card transactions.

![FraudIQ Dashboard](https://github.com/user-attachments/assets/53ddb62e-ad69-4334-8db1-4c7dbbdc63ac)

---

## 🚀 **Key Features**

- **Logistic Regression Model**  
  Trained on a dataset of 284,807 transactions with a validation accuracy of **97.5%**.

- **Risk Scoring System**  
  Assigns a fraud risk score (0–100) based on model probability, categorized into **Low**, **Medium**, or **High Risk**.

- **Real-Time Fraud Analysis**  
  Processes transaction data and returns instant risk evaluations.

- **Risk Summary Report**  
  Generates a PDF report summarizing total transactions, percentage of each risk category, and key statistics like average and max score.

- **Market Intelligence Integration**  
  Includes a dedicated button linking directly to **S&P Global’s Market Intelligence** platform for extended financial analysis.

---

## 🧑‍💻 **Tech Stack**

- **Frontend**: React.js  
  Styled to resemble the **S&P Global Market Intelligence** UI.

- **Backend**: Flask  
  REST API to serve model predictions and generate reports.

- **Machine Learning**:  
  Logistic Regression (with **SMOTE** for handling class imbalance).

---

## 📊 **How It Works**

1. **Transaction Input**  
   Users enter transaction amount and time via the React dashboard.

2. **Risk Prediction**  
   Backend returns a risk score from the trained logistic regression model, assigning a risk category.

3. **Insights Dashboard**  
   Displays results through interactive charts (built with Recharts) styled after the S&P UI.

4. **Market Intelligence Access**  
   Users can explore more financial data through a redirect to the Market Intelligence platform.

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

# Navigate to the frontend directory
cd client

# Install frontend dependencies
npm install

# Start the React frontend
npm start
