from flask import Flask, render_template, jsonify, request
# from flask.ext.runner import Runner
from keys import google_key
from direction import get_direction
from weather import get_weather
from search_location import get_place_location

app = Flask(__name__)
# runner = Runner(app)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/main")
def mainPage():
    return render_template('main.html', google_key=google_key)

@app.route("/directions", methods=['GET'])
def directions():
    pos1 = request.args.get('begin', type=str)
    pos2 = request.args.get('end', type=str)
    return jsonify(get_direction(pos1, pos2))

@app.route("/weather", methods=['GET'])
def weather():
    lat = request.args.get('lat', type=str)
    lng = request.args.get('lng', type=str)
    return jsonify(get_weather(lat, lng))

@app.route("/search", methods=['GET'])
def search():
    location = request.args.get('location', type=str)
    return jsonify(get_place_location(location))

if __name__ == "__main__":
    app.run()
    # runner.run()
