from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import numpy as np
import joblib
import os
import io
from reportlab.pdfgen import canvas


app = Flask(__name__)
CORS(app)

BASE_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_dir, 'fraud_model.pkl'))
scaler = joblib.load(os.path.join(BASE_dir, 'scaler.pkl'))
print("Model and scaler loaded successfully")


def categorize_risk_score(score):
    if score >= 70:
        return "High Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "Low Risk"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        amount = float(data.get("Amount", 0))
        time = float(data.get("Time", 0))

        input_array = np.zeros((1, 30))
        input_array[0, -2] = amount
        input_array[0, -1] = time
        input_array[:, -2:] = scaler.transform(input_array[:, -2:])

        risk_score = round(model.predict_proba(input_array)[0][1] * 100)
        risk_level = (
            "Low" if risk_score < 40 else
            "Medium" if risk_score < 70 else
            "High"
        )

        return jsonify({
            "Risk score": risk_score,
            "Risk level": risk_level
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json
    amount = data['Amount']
    time = data['Time']
    risk_score = data['Risk score']
    risk_level = data['Risk level']

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont("Helvetica", 12)

    c.drawString(100, 800, "FraudIQ Risk Analysis Report")
    c.drawString(100, 780, f"Amount: {amount}")
    c.drawString(100, 760, f"Time: {time}")
    c.drawString(100, 740, f"Risk Score: {risk_score}")
    c.drawString(100, 720, f"Risk Level: {risk_level}")
    c.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='fraud_report.pdf', mimetype='application/pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


