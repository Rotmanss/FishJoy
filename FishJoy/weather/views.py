from django.shortcuts import render
import requests
import datetime

from spots.utils import DataMixin


def weather(request):
    mixin = DataMixin()
    context = mixin.get_user_context(title='Weather')

    # API to find location to get weather data
    location = request.GET.get('loca')

    api_key = 'ad630326c3b14d8e9994e0ec7007379e'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}'

    response = requests.get(url).json()
    if response['total_results'] == 0:
        return render(request, 'weather/weather.html', context={**context, 'title': 'Weather', 'location': location,
                                                                'error': True})

    result = response['results'][0]
    latitude = result['geometry']['lat']
    longitude = result['geometry']['lng']

    # API to get current weather on this location
    key = 'd821be5ae077c5a1b9ac770bd9eb4977'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}&units=metric'

    params = {'q': location, 'appid': key, 'units': 'metric'}

    r = requests.get(url=url, params=params)
    if not r.status_code == 200:
        return render(request, 'weather/weather.html', context={**context, 'title': 'Weather', 'location': location,
                                                                'error': True})

    res = r.json()

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    wind = res['wind']['speed']
    day = datetime.date.fromtimestamp(res['dt']).strftime('%B %d %Y %I %p')

    # API to get weather forecast on this location
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={key}&units=metric'

    r = requests.get(url=url, params=params)
    if not r.status_code == 200:
        return render(request, 'weather/weather.html', context={**context, 'title': 'Weather', 'location': location,
                                                                'error': True})

    res = r.json()

    forecast = []
    for i in res['list'][:24:2]:
        forecast.append({
            'time': datetime.datetime.fromtimestamp(i['dt']).strftime('%B %d %Y %I %p'),
            'temp': i['main']['temp'],
            'wind': i['wind']['speed'],
            'icon': i['weather'][0]['icon'],
            'description': i['weather'][0]['description'],
        })

    context = {
        **context,
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'location': location,
        'pressure': pressure,
        'humidity': humidity,
        'wind': wind,
        'forecasts': forecast,
    }
    return render(request, 'weather/weather.html', context=context)
