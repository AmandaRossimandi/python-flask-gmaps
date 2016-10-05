# a file to get direction from google API

from keys import google_key
import googlemaps
from datetime import datetime

def get_direction(pos1, pos2):
    gmaps = googlemaps.Client(key=google_key)
    now = datetime.now()

    directions_result = gmaps.directions(pos1, pos2)
    # return only overview polyline
    return directions_result[0]["overview_polyline"]["points"]
