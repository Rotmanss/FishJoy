from django.urls import include, path, re_path

from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'spots', SpotsViewSet, basename='spots')
router.register(r'fish', FishViewSet, basename='fish')
router.register(r'baits', BaitsViewSet, basename='baits')
router.register(r'postman', PostmanSet, basename='postman')

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
               path('search/', search, name='search'),
               path('like_action/<slug:spot_slug>/', like_action, name='like_action'),
               path('dislike_action/<slug:spot_slug>/', dislike_action, name='dislike_action'),
               path('feedback/', Feedback.as_view(), name='feedback'),
               path('api/', include(router.urls), name='api'),
               path('api_auth/', include('rest_framework.urls')),
               path('spots_xml_export/', spots_xml_export, name='spots_xml_export'),
               path('fish_xml_export/', fish_xml_export, name='fish_xml_export'),
               path('baits_xml_export/', baits_xml_export, name='baits_xml_export'),
               path('spots_xlsx_export/', spots_xlsx_export, name='spots_xlsx_export'),
               path('fish_xlsx_export/', fish_xlsx_export, name='fish_xlsx_export'),
               path('baits_xlsx_export/', baits_xlsx_export, name='baits_xlsx_export'),
               path('create_spots_diagram/', create_spots_diagram, name='create_spots_diagram'),
               path('create_fish_diagram/', create_fish_diagram, name='create_fish_diagram'),
]
