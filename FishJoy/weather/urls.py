from django.urls import include, path, re_path

from .views import *


urlpatterns = [path('weather/', weather, name='weather')
]