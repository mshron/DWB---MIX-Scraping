import json
import requests
import re
import urllib


def geocode(address):
	'''
	>>> address = "377 Rector Place, New York City, NY"
	>>> geocode(address)
	{'lat': -1.2833333, 'city': New York, 'lng': 36.8166667, 'address': u'Nairobi, Kenya'}
	'''
	#testURL = "http://maps.googleapis.com/maps/api/geocode/json?address=Hughes%20Building,%20Kenyatta%20Avenue,%208th%20Floor,P.O%20Box%2013383%20-%2000100,%20Nairobi&sensor=false"
	baseURL = "http://maps.googleapis.com/maps/api/geocode/json?"
	data = {'address': address, 'sensor': 'false'}
	url = baseURL + urllib.urlencode(data)
	page = requests.get(url)
	x = json.loads(page.content)["results"][0]
	out = {}
	out['address'] = x["formatted_address"]
	out['lat'] = x["geometry"]["location"]["lat"]
	out['lng'] = x["geometry"]["location"]["lng"]
	out['city'] = ''
	for row in x["address_components"]:
		if (row["types"][0] == "locality") and (row["types"][1] == "political"):
			out['city'] = row["long_name"]
	return out
