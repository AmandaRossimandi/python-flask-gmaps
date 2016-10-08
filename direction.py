# a file to get direction from google API

from keys import google_key
import googlemaps
from datetime import datetime

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
    result = {
        "points": directions_result[0]["overview_polyline"]["points"],
        "distance": directions_result[0]["legs"][0]["distance"]
    }

    return result
