from rest_framework import serializers
from .models import *


class SpotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spots
        fields = '__all__'


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'


class BaitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baits
        fields = '__all__'
