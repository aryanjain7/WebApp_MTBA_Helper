import urllib.request   # urlencode function
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_url(place_name):
    try:
        url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        for word in place_name.split():
            url = url +  word + "+"
        return url
    except:
        print('Cannot find location.')

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = get_url(place_name)
    result = get_json(url)
    lat, lng = result['results']['geometry']['location']['lat'], result['results']['geometry']['location']['lng']
    return (lat, lng)    



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    places = get_lat_long(place_name)
    if places ['status'] != 'OK':
        warning("status=" + places['status'])
        return

    for result in places['results']:
        placeid = result['place_id']

        if detail['status'] != 'OK':
            break
        station = detail['results']['name']
        loc = detail['result']['geometry']['location']




def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    pass
