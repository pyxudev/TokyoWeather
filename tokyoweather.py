import urllib.request
import json

city_code = "130010"
url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code

headers = {'user-agent': 'Mozilla/5.0'}
response = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(response)
weather_json = json.loads(res.read())

weather = weather_json['forecasts'][0]['telop']
tem_min = weather_json['forecasts'][0]['temperature']['min']['celsius']
tem_max = weather_json['forecasts'][0]['temperature']['max']['celsius']

cor_06 = weather_json['forecasts'][0]['chanceOfRain']['T00_06']
cor_612 = weather_json['forecasts'][0]['chanceOfRain']['T06_12']
cor_1218 = weather_json['forecasts'][0]['chanceOfRain']['T12_18']
cor_1824 = weather_json['forecasts'][0]['chanceOfRain']['T18_24']

message = f"{weather}\n気温:{tem_min}-{tem_max}\n0-6: {cor_06}\n6-12: {cor_612}\n12-18: {cor_1218}\n18-24: {cor_1824}"

print(message)