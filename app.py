from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return render_template("index.html", version=APP_VERSION, env=APP_ENV)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION,
        "environment": APP_ENV
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "app": "cicd-demo",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "message": "CI/CD Pipeline Demo App"
    }), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=(APP_ENV == "development"))
