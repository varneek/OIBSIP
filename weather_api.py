import requests
import json

api_key = '4a29ff08445ca33653d638a16b3e7911'
city = input('Enter the city:- ')

data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')


if data.json()['cod'] == '404':
    print('City not found')
else:
    weather = data.json()['weather'][0]['main']
    temp = data.json()['main']['temp']
    humidity = data.json()['main']['humidity']


    print(f'Weather of {city}: {weather}')
    print(f'Temperature of {city}: {temp}°F')
    print(f'Humidity of {city}: {humidity}')
