# a file to get a place most relevant location from google API

from keys import google_key
import googlemaps

'''
get_place_location function
params:
    location_name: location name to be searched
returns dict:
    {
        "lat": latitude of place
        "lng": longitude of place
    }
'''
def get_place_location(location_name):
    gmaps = googlemaps.Client(key=google_key)

    result = None
    place_result = gmaps.places(location_name)
    if len(place_result["results"]) > 0:
        result = {
            "lat": place_result["results"][0]["geometry"]["location"]["lat"],
            "lng": place_result["results"][0]["geometry"]["location"]["lng"]
        }
    # result = {
    #     "points": directions_result[0]["overview_polyline"]["points"],
    #     "distance": directions_result[0]["legs"][0]["distance"]
    # }

    return result
