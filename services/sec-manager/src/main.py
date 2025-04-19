import os
import jwt
import datetime
from flask import Flask, request, jsonify

SECRET_KEY = os.getenv("AUTH_SECRET_KEY", "change_in_production")

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "sec_manager running"}), 200

@app.route("/login", methods=["POST"])
def login():
    """
    Basic example: "admin"/"admin".
    """
    username = request.json.get("username")
    password = request.json.get("password")

    if username == "admin" and password == "admin":
        payload = {
            "sub": username,
            "role": "admin",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)