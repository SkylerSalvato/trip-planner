from mongoengine import Document
from mongoengine import StringField, IntField, ListField, EmbeddedDocumentListField
from .day import Day

class Itinerary(Document):
    location_based_title = StringField()
    mapped_location = StringField() # Broad or Specific (Europe, Italy, Cervinia)
    number_of_days = IntField()
    activity_categories = ListField(StringField())
    labels = ListField(StringField())
    notes = StringField()
    days = EmbeddedDocumentListField(Day)