from weather_forecast.reservamos_gateway.api_gateway import ReservamosAPIGateway
from weather_forecast.openweather.api_gateway import OpenWeatherAPIGateway

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

    def get_forecast_by_city(self):
        cities = self.search_city()
        open_water_api = OpenWeatherAPIGateway()
        forecast_response = []
        for city in cities:
            forecast = open_water_api.get_forecast(city.lat, city.long)
            temp_dict = []
            if forecast and forecast.forecast:
                for data in forecast.forecast:
                    temp_dict.append({
                        'temp_min': data.get('main').get('temp_min'),
                        'temp_max': data.get('main').get('temp_max'),
                        'date': data.get('dt_txt')
                    })
                    print(temp_dict)
            forecast_response.append({
                'city': city.city_name,
                'forecast': temp_dict
            })

        schema = ForecastSchema(many=True)
        forecast_data = schema.dump(forecast_response)
        return forecast_data
