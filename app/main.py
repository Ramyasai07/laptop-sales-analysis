from flask import Flask, jsonify, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Tiny training set: [ram_gb, ssd_gb, cpu_score] -> price
X = np.array([[4, 256, 4], [8, 512, 6], [8, 1024, 7],
              [16, 512, 8], [16, 1024, 9], [32, 1024, 10]])
y = np.array([30000, 45000, 55000, 75000, 90000, 130000])
model = LinearRegression().fit(X, y)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.post("/predict")
def predict():
    d = request.get_json(force=True)
    features = [[d["ram"], d["ssd"], d["cpu_score"]]]
    price = float(model.predict(features)[0])
    return jsonify(price=round(price, 2))
