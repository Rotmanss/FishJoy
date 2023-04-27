from django.test import TestCase, RequestFactory

from ..views import map_app


class MapTest(TestCase):
    def test_map(self):
        factory = RequestFactory()
        request = factory.get('/map/', {'spot': 'London'})
        response = map_app(request)
        self.assertEqual(response.status_code, 200)
