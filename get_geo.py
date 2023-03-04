import requests
from flask import request
import os

def lat_lng(location):
  # API call to get latitude and longitude values of user location
  # api_key = os.environ.get('MAP_QUEST_KEY')

  parameters = {
      'key': 'L4GMh0c4OsJjEBxvlhFkrGCwwdOuzblt',
      'location': location
      }
  response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
  data = response.json()

  lat = data['results'][0]['locations'][0]['latLng']['lat']
  long = data['results'][0]['locations'][0]['latLng']['lng']

  print(lat, long)

  return lat, long