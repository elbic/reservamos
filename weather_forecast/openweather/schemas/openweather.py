from marshmallow import Schema, fields, EXCLUDE, post_load
from ..models.forecast import ForecastModel

class MainSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    temp_min = fields.Decimal()
    temp_max = fields.Decimal()


class CitySchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()


class WeatherSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    main = fields.Nested(MainSchema)
    dt_txt = fields.DateTime()



class ForecastSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    #city_name = fields.Str(default="")
    #lat = fields.Str(default="", allow_none=True)
    #long = fields.Str(default="", allow_none=True)
    list = fields.Nested(WeatherSchema, many=True)
    city = fields.Nested(CitySchema)

    @post_load
    def make_forecast(self, data, **kwargs):
        return ForecastModel(**data)
