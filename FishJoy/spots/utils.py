from django.core.cache import cache
from django.db.models import Count

from .models import *

about = {'button': 'About', 'url_button': 'about'}

sidebar = [{'button': 'Spots', 'url_button': 'home'},
           {'button': 'Fish', 'url_button': 'fish'},
           {'button': 'Baits', 'url_button': 'baits'}]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        context['about'] = about
        context['sidebar'] = sidebar
        context['spots_category'] = SpotCategory.objects.all()
        context['fish_category'] = FishCategory.objects.all()
        return context
