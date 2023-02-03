from django.urls import include, path, re_path

from .views import *

urlpatterns = [path('', FisherHome.as_view(), name='home'),
               path('fish/', ShowFish.as_view(), name='fish'),
               path('baits/', ShowBaits.as_view(), name='baits'),
               path('spot/<slug:spot_slug>/', ShowSpot.as_view(), name='spot'),
               path('fish/<slug:single_fish_slug>/', ShowSingleFish.as_view(), name='single_fish'),
               path('spot_category/<slug:spots_category_slug>/', ShowSpotsCategory.as_view(), name='spots_category'),
               path('fish_category/<slug:fish_category_slug>/', ShowFishCategory.as_view(), name='fish_category'),
               path('add_spot/', AddSpot.as_view(), name='add_spot'),
               path('add_fish/', AddFish.as_view(), name='add_fish'),
               path('add_bait/', AddBait.as_view(), name='add_bait'),
               path('about/', about, name='about'),
               path('register/', RegisterUser.as_view(), name='register'),
               path('login/', LoginUser.as_view(), name='login'),
               path('logout/', logout_user, name='logout'),
               path('search/', search, name='search')
]
