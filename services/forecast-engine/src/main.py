from flask import Flask, request, jsonify
from forecast import train_forecast_model, create_forecast
from anomaly import detect_anomalies
from model_store import model_repo

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "forecast_engine running"}), 200

@app.route("/train_forecast", methods=["POST"])
def train_forecast():
    """
    Expects JSON: {
      "data": [
        {"date": "2023-01-01", "revenue": 1000},
        {"date": "2023-01-02", "revenue": 1200}
      ]
    }
    """
    data = request.json.get("data", [])
    model = train_forecast_model(data)
    model_repo["forecast"] = model
    return jsonify({"message": "Forecast model trained"}), 200

@app.route("/predict_forecast", methods=["GET"])
def predict_forecast():
    days = int(request.args.get("days", 30))
    model = model_repo.get("forecast")
    if not model:
        return jsonify({"error": "No model found"}), 400
    fcst = create_forecast(model, days)
    return fcst.to_json(orient="records"), 200

@app.route("/detect_anomalies", methods=["POST"])
def detect_outliers():
    """
    Expects JSON: {
      "data": [12.5, 13.1, 9999.0, 14.2, 13.6]
    }
    """
    data = request.json.get("data", [])
    labels = detect_anomalies(data)
    return jsonify({"labels": labels.tolist()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)