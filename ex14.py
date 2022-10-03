import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key_url = '&key=AIzaSyBQr3WBCue-BcotVhidmt-tqql7pS17yrQ'

while True:
    address = input('Enter Location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address}) + api_key_url

    print('Retrieving {}'.format(url))
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved {} characters'.format(len(data)))

    try:
        js = json.loads(data)
    except Exception:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===Failure to Retrieve===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js["results"][0]["formatted_address"]
    print('Latitude: {}\tLongitude: {}'.format(lat, lng))
    print('Localização: {}'.format(location))
    