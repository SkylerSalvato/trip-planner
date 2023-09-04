from mongoengine import EmbeddedDocument
from mongoengine import StringField, LazyReferenceField, ListField, DateTimeField, BooleanField

from .user import User

class ToDoItem(EmbeddedDocument):
    associated_users = ListField(LazyReferenceField(User))
    description = StringField()
    due_date = DateTimeField()
    active = BooleanField(default=True)
    priority = StringField(default='Normal')
