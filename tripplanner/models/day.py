from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentField, ListField, LazyReferenceField, StringField
from .activity import Activity
from .route import Route

class Day(EmbeddedDocument):
    route = EmbeddedDocumentField(Route)
    activities = ListField(LazyReferenceField(Activity))
    notes = StringField()
