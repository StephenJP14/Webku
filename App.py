from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

app = Flask(__name__)
@app.route('/')
def index():
    res = {'message': 'ok!', 'status': 200, 'data': 'Hello World!'}
    return jsonify(res)

app.run()