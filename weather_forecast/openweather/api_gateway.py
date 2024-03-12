import requests
from django.conf import settings
from marshmallow import Schema, fields, ValidationError
from collections import defaultdict
from .schemas.openweather import ForecastSchema
from pprint import pprint

NUMBER_OF_TIMESTAMPS = 7

class OpenWeatherAPIGateway:
    def __init__(self):
        self.api_url = getattr(settings, "OPENWEATHER_API_URL", None)
        self.api_key = getattr(settings, "OPENWEATHER_API_KEY", None)

    def make_request(self, resource=None, data=None):
        payload = data
        forecast_data = requests.get(self.api_url, params=payload)
        result = self.load_data(forecast_data.text)
        return result

    def get_forecast(self, lat=None, lon=None):
        payload = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'cnt': NUMBER_OF_TIMESTAMPS
        }
        forecast_data = self.make_request(data=payload)
        return forecast_data

    def load_data(self, forecast_data):
        schema = ForecastSchema()
        try:
            result = schema.loads(forecast_data)
        except ValidationError as err:
            pprint(err)
        return result
