import os
import jwt
from flask import request, jsonify

SECRET_KEY = os.getenv("AUTH_SECRET_KEY", "change_in_production")

def token_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Missing token"}), 401
        try:
            token = auth_header.split()[1]
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # Optionally attach user info to request context
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return wrapper