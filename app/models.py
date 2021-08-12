from django.db import models

import requests

#Get api key
f = open("api_key.txt", "r")
api_key = f.read()

#Set endpoint and header
endpoint = 'https://api.yelp.com/v3/businesses/search'
header = {'Authorization': 'bearer %s' % api_key}

#Get parameters for the search
parameters = {'categories': 'CHANGE ME',
              'location': 'CHANGE ME',
              'price': 'CHANGE ME',
              'open_now': True}

#Send a response to the API
response = requests.get(url=endpoint, params=parameters, headers=header)
