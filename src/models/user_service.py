from src.factory.validation import Validator
from src.factory.database import Database

class User_service(object):
    def __init__(self):
        self.validator = Validator
        self.db = Database

        self.collection_name = 'boards'

        self.fields = {
            'username': 'string',
            'pwd': 'string',
            'nickname': 'string',
            'register_date': 'datetime'
        }

        self.create_required_fields = ['username', 'pwd', 'register_date']
        self.create_optional_fields = []



