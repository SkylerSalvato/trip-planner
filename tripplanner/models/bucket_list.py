from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, IntField

class BucketListItem(EmbeddedDocument):
    target_season = StringField()
    target_year = IntField()
    location_based_title = StringField()
    mapped_location = StringField() # Broad or Specific (Europe, Italy, Cervinia)