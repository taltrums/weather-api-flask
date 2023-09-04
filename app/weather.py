import requests, os
from flask import jsonify
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variables
API_KEY = os.getenv("API_KEY")

def get_weather_data(city):
    try:
        url = f'https://weatherapi-com.p.rapidapi.com/current.json?q={city}'
        headers = {
            'X-RapidAPI-Key': API_KEY,
            'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        weather = data['current']['temp_c']
        latitude = data['location']['lat']
        longitude = data['location']['lon']
        city_name = data['location']['name']

        return weather, latitude, longitude, city_name

    except Exception as e:
        print(f"Error retrieving weather data: {e}")
        return None

def generate_json_response(weather, latitude, longitude, city_name):
    response = {
        'Weather': f'{weather} C',
        'Latitude': str(latitude),
        'Longitude': str(longitude),
        'City': city_name
    }
    return jsonify(response)

def generate_xml_response(weather, latitude, longitude, city_name):
    root = Element('root')

    temperature = SubElement(root, 'Temperature')
    temperature.text = str(weather)

    city = SubElement(root, 'City')
    city.text = city_name

    lat = SubElement(root, 'Latitude')
    lat.text = str(latitude)

    lon = SubElement(root, 'Longitude')
    lon.text = str(longitude)

    xml_str = minidom.parseString(tostring(root)).toprettyxml(indent="    ")
    return xml_str
