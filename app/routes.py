from flask import jsonify, request
from app.weather import get_weather_data, generate_json_response, generate_xml_response
from app import app

@app.route('/getCurrentWeather', methods=['POST'])
def get_current_weather():
    city = request.json['city']
    output_format = request.json['output_format']

    weather_data = get_weather_data(city)
    if weather_data is None:
        return jsonify({'error': 'Failed to retrieve weather data.'}), 500

    weather, latitude, longitude, city_name = weather_data

    if output_format == 'json':
        return generate_json_response(weather, latitude, longitude, city_name)
    elif output_format == 'xml':
        return generate_xml_response(weather, latitude, longitude, city_name)
    else:
        return jsonify({'error': 'Invalid output format.'}), 400
