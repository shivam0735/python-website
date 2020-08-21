from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__,
        static_url_path="",
        static_folder='website')


global_history = []
@app.route("/")
def home():
    url_for_index = url_for('static', filename='index.html')
    return redirect(url_for_index)


@app.route('/backend')
def hello():
    return "Hello World!"

@app.route('/backend/greeting/<name>')
def greeting(name):
    if name not in global_history:
        global_history.append(name)
    return "Hello! " + name

@app.route('/backend/history')
def get_global_history():
    return jsonify(global_history)

@app.route('/backend/square/<number>')
def square_(number):
    number=int(number)
    return str(number*number)

@app.route('/abcd/efgh/small_html.html')
def small_html():
    return "<html><body><h1>Hello</h1></body></html>"

youtube_songs = {
    "bohemian rhapsody" : "vsl3gBVO2k4",
    "wow" : "393C3pr2ioY",
    "rockstar" : "UceaB4D0jpo"
}

@app.route('/backend/song_search')
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
