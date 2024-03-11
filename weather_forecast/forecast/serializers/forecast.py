from marshmallow import Schema, fields, EXCLUDE, post_load

class ForecastSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    city_name = fields.Str(default="")
