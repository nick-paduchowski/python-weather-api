# Python-weather-api

This is a very simple python weather API I am developing. This is an easier way to access the MeteoFranceAPI for web developers. It can fetch up to 15 days in the future. 

After cloning the script and installing the required dependencies, run the script and point your browser to http://localhost:45698 to use it.

The API will return JSON data. All endpoints require both a lat and a long parameter.

/forecast returns current weather data and 3 hourly forecast for 15 days.

/daily-forecast returns daily outlook for the next 15 days.

To do:

- Add rain alerts
- Add extreme weather alerts
- Add input validation for parameters
