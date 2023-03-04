import requests
import os
import logging
from pprint import pprint

def get_restaurants_data(location):
  try:
    url = "https://api.yelp.com/v3/businesses/search"
    api_key = os.environ.get('TEST_YELP_KEY')

    headers = { "Authorization": "Bearer " + api_key}

    parameters = {'location': '%s' % location,
                  'term': 'restaurants',
                  'radius': 40000,
                  'limit': 10,
                  'sort_by': 'best_match' 
                  }

    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 404: # not found
      return None, f'Location {location} not found'
    response.raise_for_status()
    data = response.json()
    businesses = data['businesses']
    restaurants_data = extract_restaurants_data(businesses)

    return restaurants_data, None # return data, error
  
  except Exception as e:
    logging.exception(e)
    return None, 'Error connecting to Yelp API.'


def extract_restaurants_data(businesses):
  business_list = []

  for business in businesses:
    full_address = str(business['location']['display_address'])
    full_address = full_address.replace("[","")
    full_address = full_address.replace("]","")
    full_address = full_address.replace("'","")
    latitude = business['coordinates']['latitude']
    longitude = business['coordinates']['longitude']

    business_values = {
      'image': business['image_url'],
      'name': business['name'],
      'phone': business['display_phone'],
      'full_address': full_address,
      'rating': business['rating'],
      'review_count': business['review_count'],
      'url': business['url'],
      'latitude': latitude,
      'longitude': longitude
    }
    business_list.append(business_values)
    
  return business_list
