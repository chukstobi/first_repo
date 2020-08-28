import requests

payload = {'q':'Lagos', 'APPID':'605a3f6ecadf2aba2db67fdf2721361f'}
api_key = '605a3f6ecadf2aba2db67fdf2721361f'
city_id = '2332453'
response = (f"https://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}")
fetch = requests.get(response)
wea = fetch.json()
print(wea)

# payload = {'q':'Lagos', 'APPID':'605a3f6ecadf2aba2db67fdf2721361f'}

# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)

# data = response.json()
# coord = data['coord']
# weather = data['weather'][0]
# main = data['main']
# wind = data['wind']
# bio = data['sys']
# time = data['timezone']
# name = data['name']

# print(f"Country:\n{bio}\nCoordinates:\n{coord}\nState:{name} Timezone:{time}\nTemperature:\n{main}\nWind:\n{wind}\n")
# for info in data:
#     print(data,'\n')
# print(weather)