import os
import requests

from mongoengine import EmbeddedDocument
from mongoengine import StringField, IntField

class Cost(EmbeddedDocument):
    value = IntField(default=0)
    base = StringField(default='USD')

    # def convert_to(self, other_base):
    #     conversion_api = 'http://data.fixer.io/api/latest'
    #     query_params = {
    #         'access_key': os.environ.get('FIXER_API_KEY'),
    #         'base': '', # Get self.base?
    #         'symbols': other_base
    #     }
    #     conversion_response = requests.get(conversion_api, params=query_params)

