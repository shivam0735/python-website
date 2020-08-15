from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

global_history = []

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/greeting/<name>')
def greeting(name):
    global_history.append(name)
    return "Hello! " + name

@app.route('/history')
def get_global_history():
    return jsonify(global_history)

app.run(debug=True, host="0.0.0.0")