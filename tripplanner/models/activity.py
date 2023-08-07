from mongoengine import Document, EmbeddedDocument

class ActivityInfo(Document):
    pass

class Activity(EmbeddedDocument):
    pass