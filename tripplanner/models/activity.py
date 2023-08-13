from mongoengine import Document, EmbeddedDocument
from mongoengine import (StringField, URLField, EmbeddedDocumentField, ListField,
                         IntField, BooleanField, DateTimeField, EmbeddedDocumentListField)
from .location import Location, ConnectionAirport
from .cost import Cost

class ActivityDetails(EmbeddedDocument):
    meta = {
        'abstract': True
    }
    activity_type = StringField()

class LodgingActivity(ActivityDetails):
    nights_staying = IntField(min_value=1)
    check_in = DateTimeField()
    check_out = DateTimeField()
    location = EmbeddedDocumentField(Location)
    notable_amenities = StringField()

class TransportActivity(ActivityDetails):
    source_timezone = StringField()
    destination_timezone = StringField()

class PlaneTransport(TransportActivity):
    flight_number = StringField()
    departure_airport = EmbeddedDocumentField(Location)
    arrival_airport = EmbeddedDocumentField(Location)
    departure_terminal = StringField()
    arrival_terminal = StringField()
    connection_airports = EmbeddedDocumentListField(ConnectionAirport) # Figure out how to enforce order. Index? Time of departure?

class PublicTransport(TransportActivity):
    line = StringField()
    source_stop_name = StringField()
    destination_stop_name = StringField()
    ticket_type = StringField() # Paper-Validate, On-Bus, Electronic, etc.
    public_transport_type = StringField()

class BusTransport(PublicTransport):
    pass

class TrainTransport(PublicTransport):
    pass

class BoatTransport(PublicTransport):
    pass

class CarTransport(TransportActivity):
    category = StringField() # Rental or Private Transfer

class DestinationActivity(ActivityDetails):
    start_time = DateTimeField()
    end_time = DateTimeField()
    time_at_destination = DateTimeField()

class TourDestination(DestinationActivity):
    tour_guide_name = StringField()
    tour_guide_phone_number = StringField()
    tour_guide_email = StringField()

class Activity(Document):
    name = StringField(required=True)
    labels = ListField(StringField())
    images = ListField(URLField())
    details = EmbeddedDocumentField(ActivityDetails)
    notes = StringField()
    cost = EmbeddedDocumentField(Cost)
    active = BooleanField(default=True)