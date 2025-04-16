import {useState} from "react";
import { BarChart, XAxis, YAxis, Tooltip, Bar, ResponsiveContainer } from "recharts";
import './App.css';

const FraudIQDashboard = () => {
  const [transactionAmount, setTransactionAmount] = useState("");
  const [transactionTime, setTransactionTime] = useState("")
  const [riskData, setRiskData] = useState([
    {name: "Low Risk", value: 60},
    {name: "Medium Risk", value: 25},
    {name: "High risk", value: 15},
  ]);

  const [riskScore, setRiskScore] = useState(null);
  const [riskLevel, setRiskLevel] = useState(null);

  const [alerts, setAlerts] = useState([
    { id: "TXN12345", level: "High" },
    { id: "TXN67890", level: "Medium" },
  ]);

  const handleAnalyzeRisk = async () => {
    if (!transactionAmount || !transactionTime){
      alert("Please enter both the transaction time and amount.");
      return;
    }

    try{
      const transactionData = {
        Amount: transactionAmount,
        Time: transactionTime,
      };

    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(transactionData)
    });

    console.log("Response status:", response.status);
    const result = await response.json();
    console.log("Received:", result);


    if (response.ok) {
      setRiskScore(result["Risk score"]);
      setRiskLevel(result["Risk level"])

      setRiskData([
        { name: "Low Risk", value: 100 - result["Risk score"] },
        { name: "Medium Risk", value: 30 },
        { name: "High Risk", value: result["Risk score"] },
      ]);

    } else {
      alert(`Error: ${result.error}`);
    }

  } catch (error) {
    alert("An error occurred. Please try again.");
    console.error(error);
  }
};

const handleReport = async () => {
  if (riskScore === null || riskLevel === null) {
    alert("Please analyze a transaction before generating a report.");
    return;
  }

  const reportData = {
    Amount: transactionAmount,
    Time: transactionTime,
    "Risk score": riskScore,
    "Risk level": riskLevel,
  };

  try {
    const response = await fetch("http://localhost:5000/generate-report", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(reportData),
    });

    if (!response.ok) {
      throw new Error("Failed to generate report.");
    }

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "fraud_report.pdf";
    a.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error("Error generating report:", error);
    alert("An error occurred while generating the report.");
  }
};


const handleMarket = () => {
  window.open("https://www.spglobal.com/marketintelligence/en/", "_blank");

}

  return (
    <div className="Container">
      <h1>FraudIQ Dashboard</h1>
      <h2>Transaction Risk Analyzer</h2>
      <div className="Bar">
        <input
          type="number"
          placeholder="Transaction Amount"
          value={transactionAmount}
          onChange={(e) => setTransactionAmount(e.target.value)}
        />
        <input
        type="number"
        placeholder="Transaction Time"
        value={transactionTime}
        onChange={(e) => setTransactionTime(e.target.value)}
        />
        <button onClick={handleAnalyzeRisk} className="Button">
          Analyze Risk
        </button>
      </div>

      <div className="ChartResultContainer">
      <div className="Chart" style={{ width: "100%", maxWidth: "500px", margin: "auto" }}>
        <h3>Risk Distribution</h3>
        <ResponsiveContainer width="100%" height={200}>
          <BarChart data={riskData}>
            <XAxis dataKey={"name"}/>
            <YAxis/>
            <Tooltip/>
            <Bar dataKey="value" fill="#D6002A" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="Result">
        <h3>Result Analysis</h3>
        <p>Risk Score: {riskScore}%</p>
        <p>Risk Level: {riskLevel}</p>
        <button onClick={handleReport} className="Report">Generate Report</button>
      </div>
      </div>
      <div className="FooterButton">
      <button onClick={handleMarket} className="Market" >S&P Market Intelligence </button>
      </div>
    </div>
  );
}

export default FraudIQDashboard;
