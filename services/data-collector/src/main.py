from flask import Flask, jsonify, request
import os

from quickbooks_api import fetch_quickbooks_data
from stripe_api import fetch_stripe_data
from salesforce_api import fetch_salesforce_data

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "data_collector running"}), 200

@app.route("/collect/quickbooks", methods=["POST"])
def collect_quickbooks():
    try:
        data = fetch_quickbooks_data()
        # TODO: Push data to Kafka, or do something with it
        return jsonify({"message": "QuickBooks data collected", "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/collect/stripe", methods=["POST"])
def collect_stripe():
    try:
        data = fetch_stripe_data()
        # TODO: ...
        return jsonify({"message": "Stripe data collected", "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/collect/salesforce", methods=["POST"])
def collect_salesforce():
    try:
        data = fetch_salesforce_data()
        return jsonify({"message": "Salesforce data collected", "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)