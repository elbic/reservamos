from weather_forecast.reservamos_gateway.api_gateway import ReservamosAPIGateway
from weather_forecast.forecast.serializers.forecast import ForecastSchema
class CityAdapter:
    def __init__(self, city_name=None):
        self.city_name = city_name
        self.city_list = []

    def is_valid(self):
        return True

    def search_city(self):
        cities = ReservamosAPIGateway()
        data = cities.get_cities(self.city_name)
        return data

    def get_forecast(self):
        data = self.search_city()
        schema = ForecastSchema(many=True)
        forecast_data = schema.dump(data)
        return forecast_data
