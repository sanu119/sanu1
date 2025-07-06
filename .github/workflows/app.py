from flask import Flask, jsonify
import datetime
import random

app = Flask(_name_)

@app.route("/")
def home():
    return "<h1>🚀 DevOps Dashboard API</h1><p>Try /status to see CI/CD pipeline info.</p>"

@app.route("/status")
def status():
    stages = ["Build", "Test", "Deploy"]
    results = ["Success", "Failed", "Running", "Queued"]

    pipeline_data = {
        "pipeline_id": random.randint(1000, 9999),
        "project": "DevOps-Demo",
        "status": random.choice(results),
        "last_run": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "stages": {
            stage: random.choice(results) for stage in stages
        }
    }
    return jsonify(pipeline_data)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
