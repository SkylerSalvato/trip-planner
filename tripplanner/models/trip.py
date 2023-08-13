from mongoengine import Document
from mongoengine import StringField, DateTimeField, LazyReferenceField, ListField, EmbeddedDocumentListField

from .reservation import Reservation
from .itinerary import Itinerary
from .user import User

class Trip(Document):
    creator = LazyReferenceField(User)
    users_on_trip = ListField(LazyReferenceField(User))
    reservations = EmbeddedDocumentListField(Reservation)
    labels = ListField(StringField())
    start_date = DateTimeField()
    end_date = DateTimeField()
    active_itinerary = LazyReferenceField(Itinerary)
    itinerary_options = ListField(LazyReferenceField(Itinerary))