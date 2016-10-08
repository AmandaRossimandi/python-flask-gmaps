# a file to get direction from google API

from keys import google_key
import googlemaps
from datetime import datetime
import math

'''
get_direction function
params:
    pos1: begin point coordinates, str with latitude and longitude separated by comma, e.g. -6.29384,5.221
    pos2: end point coordinates, str with latitude and longitude separated by comma, e.g. -6.29384,5.221
returns dict:
    {
        "points": encoded points for direction polyline in str
        "distance": {
            "text": direction distance in str, e.g. "12 km"
            "value": direction distance in int in meters
        }
    }
'''
def get_direction(pos1, pos2):
    gmaps = googlemaps.Client(key=google_key)
    now = datetime.now()

    directions_result = gmaps.directions(pos1, pos2, mode="walking")

    pos1_latlng = {
        "lat": float(pos1.split(',')[0]),
        "lng": float(pos1.split(',')[1])
    }

    pos2_latlng = {
        "lat": float(pos2.split(',')[0]),
        "lng": float(pos2.split(',')[1])
    }

    result = {
        "begin": pos1_latlng,
        "end": pos2_latlng,
        "distance": {"value": calculate_distance(pos1_latlng, pos2_latlng)},
        "result": directions_result
    }

    if len(directions_result) > 0:
        result = {
            "points": directions_result[0]["overview_polyline"]["points"],
            "distance": directions_result[0]["legs"][0]["distance"],
            "result": directions_result
        }

    return result

def calculate_distance(pos1, pos2):
    dlng = math.radians(pos2["lng"]-pos1["lng"])
    dlat = math.radians(pos2["lat"]-pos1["lat"])
    R = 6373000
    a = (math.sin(dlat/2))**2 + math.cos(math.radians(pos1["lat"])) * math.cos(math.radians(pos2["lat"])) * (math.sin(dlng/2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c

    return int(d)
