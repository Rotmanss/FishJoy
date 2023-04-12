from django.shortcuts import render
import folium
import requests

from spots.utils import DataMixin


def map_app(request):
    mixin = DataMixin()
    context = mixin.get_user_context(title='Map')

    location = request.GET.get('spot')

    api_key = 'ad630326c3b14d8e9994e0ec7007379e'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}'

    response = requests.get(url).json()
    if response['total_results'] == 0:
        return render(request, 'map/map.html', context={**context, 'title': 'Map', 'location': location, 'error': True})

    result = response['results'][0]

    latitude = result['geometry']['lat']
    longitude = result['geometry']['lng']
    city = result['components']['city'] if 'city' in result['components'] else location

    map = folium.Map(zoom_start=10)
    folium.Marker([latitude, longitude], tooltip='Click for more', popup=city).add_to(map)

    map = map._repr_html_()
    context = {**context, 'map': map, 'error': False}

    return render(request, 'map/map.html', context=context)
