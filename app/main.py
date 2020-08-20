from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

global_history = []

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/greeting/<name>')
def greeting(name):
    if name not in global_history:
        global_history.append(name)
    return "Hello! " + name

@app.route('/history')
def get_global_history():
    return jsonify(global_history)

@app.route('/square/<number>')
def square_(number):
    number=int(number)
    return str(number*number)

youtube_songs = {
    "bohemian rhapsody" : "vsl3gBVO2k4",
    "wow" : "393C3pr2ioY",
    "rockstar" : "UceaB4D0jpo"
}

@app.route('/song_search')
def search_song():
    input_string = request.args.get('input_string')
    if input_string is None:
        return "NA"
    input_string = input_string.lower()
    if input_string in youtube_songs:
        return youtube_songs[input_string]
    else:
        return "NA"

app.run(debug=True, host="0.0.0.0")
