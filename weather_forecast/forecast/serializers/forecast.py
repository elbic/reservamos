from marshmallow import Schema, fields, EXCLUDE, post_load


class WeatherSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    date = fields.DateTime()
    temp_min = fields.Decimal()
    temp_max = fields.Decimal()


class ForecastSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    city = fields.Str(default="")
    forecast = fields.Nested(WeatherSchema, many=True)

#    @post_load
#    def make_forecast(self, data, **kwargs):
#        return ForecastModel(**data)
