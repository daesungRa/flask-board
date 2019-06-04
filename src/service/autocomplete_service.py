from src.factory.validation import Validator
from src.factory.database import Database

class Autocomplete_service(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.collection_name = 'countries'  # default collection name

    def find(self, element, collection_name=None):
        if collection_name:
            self.collection_name = collection_name
        find_result = self.db.find(element, self.collection_name, projection={'name': 'true', 'code': 'true'}, limit=20)

        return find_result



