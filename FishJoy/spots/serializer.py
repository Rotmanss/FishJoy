from rest_framework import serializers
from .models import *


class SpotsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Spots
        fields = '__all__'
        read_only_fields = ['likes', 'dislikes', 'liked_by', 'disliked_by']
        extra_kwargs = {
            'photo': {'required': True}
        }

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        if self.context['request'].method == 'PUT':
            extra_kwargs['photo']['required'] = False
            self.Meta.read_only_fields += ['rating']
        return extra_kwargs


class FishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Fish
        fields = '__all__'
        extra_kwargs = {
            'photo': {'required': True}
        }

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        if self.context['request'].method == 'PUT':
            extra_kwargs['photo']['required'] = False
        return extra_kwargs


class BaitsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Baits
        fields = '__all__'
        extra_kwargs = {
            'photo': {'required': True}
        }

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        if self.context['request'].method == 'PUT':
            extra_kwargs['photo']['required'] = False
        return extra_kwargs
