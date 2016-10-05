from flask import Flask, render_template, jsonify, request
from keys import google_key
from direction import get_direction

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/main")
def mainPage():
    return render_template('main.html', google_key=google_key)

@app.route("/directions")
def directions():
    pos1 = request.args.get('begin', type=str)
    pos2 = request.args.get('end', type=str)
    return jsonify(get_direction(pos1, pos2))

if __name__ == "__main__":
    app.run(debug=True)
