from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, generics
from .adapters.forecast import CityAdapter

class ForecastViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request, city=None):
        city_adapter = CityAdapter(city_name=city)
        city_forecast = city_adapter.get_forecast_by_city()
        return Response(city_forecast)
