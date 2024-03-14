
""""
Program: Assignment2.py
Programmer: Matias Moretti
This is a request API for Assignment 2 of Python

"""
import requests

api_key = '2ced364219ff1ee59bc33df10ddc222e'

city = input('Enter city name: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+api_key
response = requests.get(url)
print(response.text)
if response.status_code == 200:
    data = response.json()
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    temp = data['main']['temp']
    visibility = data['visibility']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']
    print(f'Minimum Temperature: {temp_min}')
    print(f'Maximum Temperature: {temp_max}')
    print(f'Temperature: {temp}')
    print(f'Visibility: {visibility}')
    print(f'Wind Speed: {wind_speed}')
    print(f'Country: {country}')
else:
    print('Error fetching weather data')