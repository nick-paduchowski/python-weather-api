from flask import *
import json
from collections import OrderedDict
from meteofrance_api import MeteoFranceClient

app = Flask(__name__)

client = MeteoFranceClient()

@app.route('/', methods=['GET'])
def request_page1():
    data_set = {'API Home ': 'Welcome to The Weather API'}

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
                          'humidity': hour['humidity'],
                          'windspeed': hour['wind']['speed'],
                          'rain': hour['rain']['6h'],
                          })


    response = jsonify(data_set = {
        'hourly': hourlyArray
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/daily-forecast/', methods=['GET'])
def request_page2():

    latitude = request.args.get('lat')
    longitude = request.args.get('long')

    forecast = client.get_forecast(latitude,longitude,language="en")

    current_forecast = forecast.current_forecast
    daily_forecast = forecast.daily_forecast
    # rain = forecast.Rain()

    response = jsonify(data_set ={
        'current': {
            'time': current_forecast['dt'],
            'temp': current_forecast['T']['value'],
            'feelslike': current_forecast['T']['windchill'],
            'humidity': current_forecast['humidity'],
            'dewPoint': current_forecast['T']['value'] - ((100 - current_forecast['humidity']) / 5),
            'desc': daily_forecast[0]['weather12H']['desc']
        },
        #'dailyForecast': daily_forecast,
        'dailyForecast': {
            'day1': {
                'time': daily_forecast[0]['dt'],
                'maxTemp': daily_forecast[0]['T']['max'],
                'minTemp': daily_forecast[0]['T']['min'],
                'humidity': (daily_forecast[0]['humidity']['max'] + daily_forecast[0]['humidity']['min']) / 2,
                'desc': daily_forecast[0]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[0]['precipitation']['24h']
            },
            'day2': {
                'time': daily_forecast[1]['dt'],
                'maxTemp': daily_forecast[1]['T']['max'],
                'minTemp': daily_forecast[1]['T']['min'],
                'humidity': (daily_forecast[1]['humidity']['max'] + daily_forecast[1]['humidity']['min']) / 2,
                'desc': daily_forecast[1]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[1]['precipitation']['24h']
            },
            'day3': {
                'time': daily_forecast[2]['dt'],
                'maxTemp': daily_forecast[2]['T']['max'],
                'minTemp': daily_forecast[2]['T']['min'],
                'humidity': (daily_forecast[2]['humidity']['max'] + daily_forecast[2]['humidity']['min']) / 2,
                'desc': daily_forecast[2]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[2]['precipitation']['24h']
            },
            'day4': {
                'time': daily_forecast[3]['dt'],
                'maxTemp': daily_forecast[3]['T']['max'],
                'minTemp': daily_forecast[3]['T']['min'],
                'humidity': (daily_forecast[3]['humidity']['max'] + daily_forecast[3]['humidity']['min']) / 2,
                'desc': daily_forecast[3]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[3]['precipitation']['24h']
            },
            'day5': {
                'time': daily_forecast[4]['dt'],
                'maxTemp': daily_forecast[4]['T']['max'],
                'minTemp': daily_forecast[4]['T']['min'],
                'humidity': (daily_forecast[4]['humidity']['max'] + daily_forecast[4]['humidity']['min']) / 2,
                'desc': daily_forecast[4]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[4]['precipitation']['24h']
            },
            'day6': {
                'time': daily_forecast[5]['dt'],
                'maxTemp': daily_forecast[5]['T']['max'],
                'minTemp': daily_forecast[5]['T']['min'],
                'humidity': (daily_forecast[5]['humidity']['max'] + daily_forecast[5]['humidity']['min']) / 2,
                'desc': daily_forecast[5]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[5]['precipitation']['24h']
            },
            'day7': {
                'time': daily_forecast[6]['dt'],
                'maxTemp': daily_forecast[6]['T']['max'],
                'minTemp': daily_forecast[6]['T']['min'],
                'humidity': (daily_forecast[6]['humidity']['max'] + daily_forecast[6]['humidity']['min']) / 2,
                'desc': daily_forecast[6]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[6]['precipitation']['24h']
            },
            'day8': {
                'time': daily_forecast[7]['dt'],
                'maxTemp': daily_forecast[7]['T']['max'],
                'minTemp': daily_forecast[7]['T']['min'],
                'humidity': (daily_forecast[7]['humidity']['max'] + daily_forecast[7]['humidity']['min']) / 2,
                'desc': daily_forecast[7]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[7]['precipitation']['24h']
            },
            'day9': {
                'time': daily_forecast[8]['dt'],
                'maxTemp': daily_forecast[8]['T']['max'],
                'minTemp': daily_forecast[8]['T']['min'],
                'humidity': (daily_forecast[8]['humidity']['max'] + daily_forecast[8]['humidity']['min']) / 2,
                'desc': daily_forecast[8]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[8]['precipitation']['24h']
            },
            'day10': {
                'time': daily_forecast[9]['dt'],
                'maxTemp': daily_forecast[9]['T']['max'],
                'minTemp': daily_forecast[9]['T']['min'],
                'humidity': (daily_forecast[9]['humidity']['max'] + daily_forecast[9]['humidity']['min']) / 2,
                'desc': daily_forecast[9]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[9]['precipitation']['24h']
            },
            'day11': {
                'time': daily_forecast[10]['dt'],
                'maxTemp': daily_forecast[10]['T']['max'],
                'minTemp': daily_forecast[10]['T']['min'],
                'humidity': (daily_forecast[10]['humidity']['max'] + daily_forecast[10]['humidity']['min']) / 2,
                'desc': daily_forecast[10]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[10]['precipitation']['24h']
            },
            'day12': {
                'time': daily_forecast[11]['dt'],
                'maxTemp': daily_forecast[11]['T']['max'],
                'minTemp': daily_forecast[11]['T']['min'],
                'humidity': (daily_forecast[11]['humidity']['max'] + daily_forecast[11]['humidity']['min']) / 2,
                'desc': daily_forecast[11]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[11]['precipitation']['24h']
            },
            'day13': {
                'time': daily_forecast[12]['dt'],
                'maxTemp': daily_forecast[12]['T']['max'],
                'minTemp': daily_forecast[12]['T']['min'],
                'humidity': (daily_forecast[12]['humidity']['max'] + daily_forecast[12]['humidity']['min']) / 2,
                'desc': daily_forecast[12]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[12]['precipitation']['24h']
            },
            'day14': {
                'time': daily_forecast[13]['dt'],
                'maxTemp': daily_forecast[13]['T']['max'],
                'minTemp': daily_forecast[13]['T']['min'],
                'humidity': (daily_forecast[13]['humidity']['max'] + daily_forecast[13]['humidity']['min']) / 2,
                'desc': daily_forecast[13]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[13]['precipitation']['24h']
            },
            'day15': {
                'time': daily_forecast[14]['dt'],
                'maxTemp': daily_forecast[14]['T']['max'],
                'minTemp': daily_forecast[14]['T']['min'],
                'humidity': (daily_forecast[14]['humidity']['max'] + daily_forecast[14]['humidity']['min']) / 2,
                'desc': daily_forecast[14]['weather12H']['desc'],
                'precipitationProbability': daily_forecast[14]['precipitation']['24h']
            },
      },

    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
   app.run(port=45698)

