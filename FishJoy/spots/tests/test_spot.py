import os
from io import BytesIO

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Baits, Spots, SpotCategory, Fish, FishCategory
from ..views import FisherHome, SpotsViewSet


class SpotsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = FisherHome.as_view()

    def test_fisher_home(self):
        request = self.factory.get(reverse('home'))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class BaitsPostTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        test_photo_path = os.path.join(os.path.dirname(__file__), 'dislike.png')

        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')

        with open(test_photo_path, 'rb') as f:
            photo_data = f.read()

        photo_io = BytesIO(photo_data)

        self.bait_data = {
            'name': 'Test Bait',
            'slug': 'test-bait',
            'photo': SimpleUploadedFile(name='dislike.png', content=photo_io.getvalue(), content_type='image/jpeg'),
            'price': 10.0,
            'user': self.user,
        }

    def test_add_bait(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('add_bait'), data=self.bait_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Baits.objects.filter(name='Test Bait').exists())


# class SpotsTestCase(TestCase):
#     def setUp(self):
#         test_photo_path = os.path.join(os.path.dirname(__file__), 'dislike.png')
#
#         self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
#
#         with open(test_photo_path, 'rb') as f:
#             photo_data = f.read()
#
#         photo_io = BytesIO(photo_data)
#
#         self.baits = Baits.objects.create(
#             name='test', slug='test',
#             photo=SimpleUploadedFile(name='dislike.png', content=photo_io.getvalue(), content_type='image/jpeg'),
#             price=10.0,
#             user=self.user
#         )
#
#         self.fish = Fish.objects.create(
#             name='test', slug='test',
#             photo=SimpleUploadedFile(name='dislike.png', content=photo_io.getvalue(), content_type='image/jpeg'),
#             average_weight=32.0,
#             fish_category=FishCategory.objects.create(name='Test Category', slug='Test Category'),
#             user=self.user
#         )
#         self.fish.baits.set([self.baits])
#
#         self.spot = Spots.objects.create(
#             title='Test Spot',
#             slug='test-spot',
#             rating=5,
#             location='Test Location',
#             photo=SimpleUploadedFile(name='dislike.png', content=photo_io.getvalue(), content_type='image/jpeg'),
#             max_depth=10.0,
#             likes=0,
#             dislikes=0,
#             spot_category=SpotCategory.objects.create(name='Test Category', slug='Test Category'),
#             user=self.user,
#         )
#         self.spot.fish.set([self.fish])
#
#     def test_like_action(self):
#         # Log in as the test user
#         self.client.login(username='testuser', password='testpass')
#
#         # Call the view with a POST request
#         response = self.client.post(reverse('like_action', kwargs={'spot_slug': 'test-spot'}))
#
#         # Check that the response is a redirect
#         self.assertEqual(response.status_code, 302)
#
#         # Refresh the object from the database
#         self.spot.refresh_from_db()
#
#         # Check that the spot has one like and no dislikes
#         self.assertEqual(self.spot.likes, 1)
#         self.assertEqual(self.spot.dislikes, 0)
#
#         # Call the view again with a POST request
#         response = self.client.post(reverse('like_action', kwargs={'spot_slug': 'test-spot'}))
#
#         # Check that the response is a redirect
#         self.assertEqual(response.status_code, 302)
#
#         # Refresh the object from the database
#         self.spot.refresh_from_db()
#
#         # Check that the spot still has one like and no dislikes
#         self.assertEqual(self.spot.likes, 1)
#         self.assertEqual(self.spot.dislikes, 0)


class DRFTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = SpotsViewSet.as_view({'get': 'list'})

    def test_my_view(self):
        url = reverse('spots-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
