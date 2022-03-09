from flask import *
import json
from meteofrance_api import MeteoFranceClient

app = Flask(__name__)

client = MeteoFranceClient()

@app.route('/', methods=['GET'])
def request_page1():
    data_set = {'API Home ': 'Welcome to Nick Paduchowskis Weather API'}

    jsonData = json.dumps(data_set)

    return jsonData

@app.route('/forecast/', methods=['GET'])
def request_page():

    latitude = request.args.get('lat')
    longitude = request.args.get('long')

    forecast = client.get_forecast(latitude,longitude,language="en")

    hourly_forecast = forecast.forecast
    hourlyArray = []

    for hour in hourly_forecast:
        hourlyArray.append({'time': hour['dt'],
                            'temp': hour['T']['value'],
                            'feelslike': hour['T']['windchill'],
                            'rain': hour['rain']['6h'],
                            'humidity': hour['humidity'],
                            'windspeed': hour['wind']['speed']
                            })


    data_set = {
        'hourly': hourlyArray
    }
    jsonData = json.dumps(data_set)

    return jsonData

@app.route('/daily-forecast/', methods=['GET'])
def request_page2():

    latitude = request.args.get('lat')
    longitude = request.args.get('long')

    forecast = client.get_forecast(latitude,longitude,language="en")

    current_forecast = forecast.current_forecast
    today_forecast = forecast.today_forecast
    daily_forecast = forecast.daily_forecast

    data_set = {
        'current': current_forecast,
        'todaysForecast': today_forecast,
        'dailyForecast': daily_forecast
    }

    jsonData = json.dumps(data_set)

    return jsonData

if __name__ == '__main__':
   app.run(port=45698)

