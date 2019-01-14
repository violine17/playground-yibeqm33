import json
import urllib.request

api_key = '&key=AIzaSyBp-sJGdfd9Y_bW8WQFEdtGF54FIU0XiAk'
url_request = r'https://maps.googleapis.com/maps/api/place/textsearch/json?&location=29.952381,-90.067648&query=beignets'
url_response_as_str = urllib.request.urlopen(url_request + api_key).read()
url_response = json.loads(url_response_as_str)
for place in url_response['results']:
    print(place['name'])
    print(place['geometry']['location']['lat'], place['geometry']['location']['lng'])
    print(place['rating'])
