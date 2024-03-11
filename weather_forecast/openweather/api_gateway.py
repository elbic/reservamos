import requests
from django.conf import settings
from .schemas.city import CitySchema
from marshmallow import Schema, fields, ValidationError
from collections import defaultdict
#from .openweather.schemas import

class OpenWeatherAPIGateway:
    def __init__(self):
        self.api_url = getattr(settings, "OPENWEATHER_API_URL", None)
        self.api_key = getattr(settings, "OPENWEATHER_API_KEY", None)

    def make_request(self, resource=None, data=None):
        payload = data
        forecast_data = requests.get(self.api_url + resource, params=payload)
        result = self.load_data(forecast_data.text)
        return result

    def get_forecast(self, city=None):
        payload = {
            'lat': None,
            'lon': None,
            'appid': self.api_key
        }
        forecast_data = self.make_request(data=payload)
        return forecast_data

    def load_data(self, forecast_data):
        schema = Schema(many=True)
        try:
            result = schema.loads(forecast_data)
        except ValidationError as err:
            pprint(err)
        return result
