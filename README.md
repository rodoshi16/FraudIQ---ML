**FraudIQ - ML Risk Analysis tool** 
FraudIQ is an intelligent fraud detection tool designed to help financial institutions assess transaction risks. 

![473E4778-C793-4570-BBF0-7A046F12B711](https://github.com/user-attachments/assets/53ddb62e-ad69-4334-8db1-4c7dbbdc63ac)


🚀 **Key Features**
**Logistic Regression Model**: Implements a Logistic Regression Machine Learning model trained with a dataset of 284,807 transactions with a validation accuracy of 97.5%
**Risk Scoring System**: Assigns a probability-based fraud risk score (0-100) to transactions.
**Real-Time Fraud Analysis**: Processes transaction data and provides instant risk assessments.
**Risk Summary Report**: Click Generate Report to instantly view the Total number of transactions, Percentage of High, Medium and Low Risk along with the Average and Max scores.
**Market Intelligence Integration**: Includes a dedicated Market Intelligence button that redirects users to S&P Global’s Market Intelligence platform for further financial insights.

🧑‍💻 **Tech Stack**
**Frontend**: React.js (Styled to reflect S&P Global’s Market Intelligence UI)
**Backend**: Flask (REST API for transaction risk analysis)
**Machine Learning**: Logistic Regression with SMOTE for handling class imbalance

📊 **How It Works**
**Transaction Input**: Users enter transaction details (Amount & Time).
**Risk Prediction**: The logistic regression model calculates a risk score and categorizes transactions as Low, Medium, or High risk.
**Insights Dashboard**: View risk distribution through interactive charts styled after S&P Global’s Market Intelligence UI.
**Market Intelligence Access**: A Market Intelligence button redirects users to S&P Global’s Market Intelligence platform for additional financial insights.

🖥️ **Installation & Setup**
# Clone the repository
git clone https://github.com/your-username/FraudIQ.git
cd FraudIQ

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py

# Navigate to frontend and start React app
cd client
npm install
npm start
