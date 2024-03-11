import requests
from django.conf import settings
from .schemas.city import CitySchema
from .models import CityModel
from pprint import pprint

from marshmallow import Schema, fields, ValidationError
from collections import defaultdict

class ReservamosAPIGateway:
    def __init__(self):
        self.api_url = getattr(settings, "RESERVAMOS_API_URL", None)
        self.api_key = getattr(settings, "RESERVAMOS_API_KEY", None)

    def make_request(self, resource=None, data=None):
        payload = data
        cities_data = requests.get(self.api_url + resource, params=payload)
        result = self.load_city(cities_data.text)
        return result

    def get_cities(self, city=None):
        city = CityModel(city_name=city)
        schema = CitySchema()
        city_dump = schema.dump(city)
        payload = {'q': city_dump.get('city_name')}
        cities_data = self.make_request(resource='/places', data=payload)
        result = self.clean_data(cities_data)
        return result

    def load_city(self, cities_data):
        schema = CitySchema(many=True)
        try:
            result = schema.loads(cities_data)
        except ValidationError as err:
            pprint(err)
        return result

    def clean_data(self, cities_data):
        # TODO: Remove duplicates
        return cities_data
