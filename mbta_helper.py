import urllib.request   # urlencode function
import json
import string


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"



# A little bit of scaffolding if you want to use it

def get_url(place_name):
    '''
    This function takes a place name as a string and
    returns the associated Google API search URL
    '''
    try:
        url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        place_name = place_name.strip(string.punctuation)
        # for word in place_name.split():
        #     if url != place_name.split()[:-1]:
        #         url = url +  word + "+"
        #     else:
        #         url += word
        query = urllib.parse.quote_plus(place_name, safe='', encoding=None, errors=None)
        url += query
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
    if(result['results'] != []):
        lat, lng = result['results'][0]['geometry']['location']['lat'], result['results'][0]['geometry']['location']['lng']
        return (lat, lng) 
    else:
        print('Google could not find your location bruh. You searching for Area 51?')
    return (0,0)



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url =  "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=" + str(latitude) +  "&lon=" + str(longitude) + "&format=json"
    result = get_json(url)
    if(result["stop"] != []):
        stopname = result["stop"][0]["stop_name"]
        distance = result["stop"][0]["distance"]
        return (stopname, distance)
    else:
        print("No stations near you. Are you even in Boston?")
        return ("Area 51", 'Inf miles away')


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat, lng = get_lat_long(place_name)
    return get_nearest_station(lat, lng)

def main():
    place = input("Name a landmark near you bruh: ")
    print(find_stop_near(place))


if __name__ == '__main__':
    main()