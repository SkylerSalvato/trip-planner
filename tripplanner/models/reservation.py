from mongoengine import EmbeddedDocument
from mongoengine import StringField, DateTimeField, LazyReferenceField, BooleanField

from .activity import Activity

class Reservation(EmbeddedDocument):
    confirmation_number = StringField()
    time_based = BooleanField()
    reservation_time = DateTimeField()
    timezone = StringField()
    activity = LazyReferenceField(Activity)
