from flask import Flask, request, jsonify
from batch_etl import run_batch_etl
from streaming_etl import start_stream_processing

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "etl_manager running"}), 200

@app.route("/batch", methods=["POST"])
def batch():
    """
    Expects JSON: {
      "input_path": "s3://some-bucket/financial-data/",
      "output_path": "s3://some-bucket/processed/"
    }
    """
    input_path = request.json.get("input_path")
    output_path = request.json.get("output_path")
    run_batch_etl(input_path, output_path)
    return jsonify({"message": "Batch ETL completed"}), 200

@app.route("/stream", methods=["POST"])
def stream():
    """
    Expects JSON: { "kafka_bootstrap": "kafka:9092", "topic": "financial-data" }
    """
    kafka_bootstrap = request.json.get("kafka_bootstrap", "kafka:9092")
    topic = request.json.get("topic", "financial-data")
    start_stream_processing(kafka_bootstrap, topic)
    return jsonify({"message": "Streaming started"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)