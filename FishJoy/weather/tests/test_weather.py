from django.test import TestCase, RequestFactory

from ..views import weather


class WeatherTest(TestCase):
    def test_weather(self):
        factory = RequestFactory()
        request = factory.get('/weather/', {'loca': 'London'})
        response = weather(request)
        self.assertEqual(response.status_code, 200)
