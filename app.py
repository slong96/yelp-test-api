from flask import Flask, render_template, request
from yelp_api import get_restaurants_data
from get_geo import lat_lng
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/get_restaurants')
def get_restaurant_info():
    location = request.args.get('location_input')
    location_info, error_message = get_restaurants_data(location)
    lat, long = lat_lng(location)
    
    if error_message:
        return render_template('error.html', error=error_message)
    else:
        return render_template('index.html', lat=lat, long=long, len=len(location_info), location_info=location_info, location=location.title())


if __name__ == '__main__':
    app.run()