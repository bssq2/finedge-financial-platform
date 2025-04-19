import os
from flask import Flask, jsonify, request
from prophet import Prophet
import pandas as pd

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "forecast_engine running"}), 200

@app.route("/forecast", methods=["POST"])
def forecast():
    """
    Expects JSON of the form:
    {
      "data": [
        {"ds": "2023-01-01", "y": 100},
        {"ds": "2023-01-02", "y": 150},
        ...
      ],
      "periods": 30
    }
    """
    content = request.json
    raw_data = content.get("data", [])
    periods = content.get("periods", 30)

    df = pd.DataFrame(raw_data)
    if df.empty or "ds" not in df.columns or "y" not in df.columns:
        return jsonify({"error": "Invalid input data"}), 400

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    forecast_output = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_dict(orient='records')
    return jsonify({"forecast": forecast_output}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)