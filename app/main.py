from flask import Flask, jsonify, request, redirect, url_for, render_template
import os

app = Flask(__name__,
        static_url_path="/static",
        static_folder='website/static',
        template_folder='website/templates')

PAGE_GREETING = {
        "page_title": "Greeting",
        "navbar_label": "Greeting",
        "template": "greeting.html",
        "function": "f_greeting"
    }

PAGE_SQUARE ={
        "page_title": "Square",
        "navbar_label": "Square",
        "template": "square.html",
        "function": "f_square"
    }

PAGE_YOUTUBE = {
        "page_title": "Youtube",
        "navbar_label": "Youtube",
        "template": "youtube.html",
        "function": "f_youtube"
    }

pages = [PAGE_GREETING, PAGE_SQUARE, PAGE_YOUTUBE]

global_history = []

@app.route("/")
def home():
    return redirect(url_for('f_greeting'))

@app.route("/greeting")
def f_greeting():
    return render_template('greeting.html', pages=pages, current_page=PAGE_GREETING)

@app.route("/square")
def f_square():
    return render_template('square.html', pages=pages, current_page=PAGE_SQUARE)

@app.route("/youtube")
def f_youtube():
    return render_template('youtube.html', pages=pages, current_page=PAGE_YOUTUBE)


@app.route('/mycss/<filename>')
def mycss(filename):
    # Resolving file_path using file_name 
    if '.css' not in filename:
        # If .css not in file, add .css at the end
        file_path='website/' + filename + '.css'
    else:
        # Otherwise, leave alone
        file_path='website/'+ filename

    # Check whether file exists
    if  not os.path.exists(file_path):
        # File doesn't exist, return 404
        return "NA", 404
    
    opened_file = open(file_path)
    data = opened_file.read()
    opened_file.close()

    return data

@app.route('/render/<path>')
def render_path(path):
    return render_template(path)

@app.route('/backend')
def hello():
    message = "Hello World!"
    return render_template('first_template.html', message=message)

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
