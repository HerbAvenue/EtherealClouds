from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route("/")
def index():
    
    realTimeWeatherURL = "https://api.tomorrow.io/v4/weather/realtime?location=toronto&apikey=mpfxt9Varif1EaQMNVcFHQGhlxoKBMxq"
    forecastWeatherURL = "https://api.tomorrow.io/v4/weather/forecast?location=new%20york&apikey=mpfxt9Varif1EaQMNVcFHQGhlxoKBMxq"
    headers = {"accept": "application/json"}
    realTimeData = requests.get(realTimeWeatherURL, headers).json()
    forecastData = requests.get(forecastWeatherURL, headers).json()

    #weatherCode = realTimeData["data"]["values"]["weatherCode"]

    weather_code_to_icon = {
      0: "Unknown",
      1000: "clear_day.svg",
      1100: "mostly_clear_day.svg",
      1101: "partly_cloudy.svg",
      1102: "mostly_cloudy.svg",
      1001: "cloudy.svg",
      2000: "fog.svg",
      2100: "fog_light.svg",
      4000: "drizzle.svg",
      4001: "rain.svg",
      4200: "rain_light.svg",
      4201: "rain_heavy.svg",
      5000: "snow.svg",
      5001: "flurries.svg",
      5100: "snow_light.svg",
      5101: "snow_heavy.svg",
      6000: "freezing_drizzle.svg",
      6001: "freezing_rain.svg",
      6200: "freezing_rain_light.svg",
      6201: "freezing_rain_heavy.svg",
      7000: "ice_pellets.svg",
      7101: "ice_pellets_heavy.svg",
      7102: "ice_pellets_light.svg",
      8000: "tstorm.svg"
    }

    #TEST DATA
    weatherCodeTest = 1001

    with open('realtime.json', 'r') as file:
        realtimeTest = json.load(file)

    with open('weathercode.json', 'r') as file:
        weatherCodeIndex = json.load(file)

    with open('forecast.json', 'r') as file:
        forecastTest = json.load(file)
    
    #print(realTimeData)
    
    return render_template('index.html', 
                           realTime=realtimeTest,
                           weatherCode=weatherCodeTest,
                           forecast=forecastTest, 
                           
                           weatherCodeIndex=weatherCodeIndex,  
                           codeIcon=weather_code_to_icon,
                           )
