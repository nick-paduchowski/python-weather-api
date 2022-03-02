# Python-weather-api

This is a very simple python weather api I am developing. It can fetch up to 15 days in the future. 

After cloning the script and installing the required dependencies, you can point your browser to http://localhost:45698 to use it.

The API will return JSON data. All endpoints require both a lat and a long parameter.

/forecast returns current weather data and 3 hourly forecast for 15 days.

/daily-forecast returns daily outlook for the next 15 days.

To do:

- Add rain alerts
- Add extreme weather alerts
- Add input validation for parameters
