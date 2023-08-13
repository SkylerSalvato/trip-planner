from mongoengine import Document
from mongoengine import (StringField, EmailField, ListField, LazyReferenceField,
                         URLField)

from .itinerary import Itinerary

class User(Document):
    name = StringField()
    email = EmailField()
    credential = StringField() # ??
    family = ListField(LazyReferenceField('User'))
    favorite_itineraries = ListField(LazyReferenceField(Itinerary))
    profile_photo = URLField()
    preferences = ListField(StringField())