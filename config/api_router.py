from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from weather_forecast.forecast.views import ForecastViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("forecast/(?P<city>\w+)", ForecastViewSet, basename='forecast')


app_name = "api"
urlpatterns = router.urls
