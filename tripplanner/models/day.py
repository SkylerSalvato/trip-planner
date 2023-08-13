from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentField, EmbeddedDocumentListField, StringField
from .activity import Activity
from .route import Route

class Day(EmbeddedDocument):
    route = EmbeddedDocumentField(Route)
    activities = EmbeddedDocumentListField(Activity)
    notes = StringField()
