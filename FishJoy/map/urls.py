from django.urls import include, path, re_path

from .views import *


urlpatterns = [path('map/', map_app, name='map')
]