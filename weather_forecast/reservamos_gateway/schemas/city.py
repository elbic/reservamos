from marshmallow import Schema, fields, EXCLUDE, post_load
from ..models import CityModel

class CitySchema(Schema):
    class Meta:
        unknown = EXCLUDE

    city_name = fields.Str(default="")
    lat = fields.Str(default="", allow_none=True)
    long = fields.Str(default="", allow_none=True)

    @post_load
    def make_city(self, data, **kwargs):
        return CityModel(**data)
