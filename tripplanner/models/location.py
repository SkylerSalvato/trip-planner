from mongoengine import EmbeddedDocument
from mongoengine import StringField, URLField, PointField, DateTimeField
from mongoengine.errors import ValidationError
from openlocationcode import openlocationcode as plus_code

def validate_plus_code(value):
    check = plus_code.isValid(value)
    if check is False:
        raise ValidationError('Invalid Plus Code provided')

class Location(EmbeddedDocument):
    meta = {
        'allow_inheritance': True
    }
    address = StringField() # https://pypi.org/project/google-i18n-address/
    city = StringField()
    country_code = StringField()
    country_area = StringField() # (State)
    postal_code = StringField()
    lat_lon = PointField(auto_index=False)
    plus_code = StringField(validation=validate_plus_code) # Use for routing
    place_id = StringField() # Use for business lookup
    location_type = StringField()
    timezone = StringField()

class Business(Location):
    phone_number = StringField()
    website = URLField()

class ConnectionAirport(Business):
    time_until_next_departure = DateTimeField()