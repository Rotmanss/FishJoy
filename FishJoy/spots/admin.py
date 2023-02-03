from django.contrib import admin
from .models import *


class SpotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'spot_category', 'photo', 'location', 'max_depth', 'time_update')


class FishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fish_category', 'photo', 'average_weight')


class BaitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price')


class SpotCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class FishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


admin.site.register(Spots, SpotsAdmin)
admin.site.register(Fish, FishAdmin)
admin.site.register(Baits, BaitsAdmin)
admin.site.register(SpotCategory, SpotCategoryAdmin)
admin.site.register(FishCategory, FishCategoryAdmin)
