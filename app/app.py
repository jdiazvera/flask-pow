import requests
from flask import Flask, jsonify, request
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

@app.route('/pow', methods=["GET"])
def get_pow():
    response = requests.get(url="http://0.0.0.0/entero")
    num = response.json()["value"]
    return jsonify(value=(num * num))

