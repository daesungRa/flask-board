from src.factory.validation import Validator
from src.factory.database import Database
from src.factory.pagination import Pagination

class Board_service(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.collection_name = 'boards' # default collection name
        self.fields = {
            "title": "string",
            "author": "string",
            "content": "string",
            "created": "datetime",
            "updated": "datetime",
        }
        self.create_required_fields = ["title", "author", "content"]
        self.create_optional_fields = []
        self.update_required_fields = ["title", "content"]
        self.update_optional_fields = []
        self.pagination = Pagination()

    def modify_fields(self, fields, create_required_fields, update_required_fields, create_optional_fields=None, update_optional_fields=None):
        self.fields = fields
        self.create_required_fields = create_required_fields
        self.update_required_fields = update_required_fields

        if create_optional_fields is not None:
            self.create_optional_fields = create_optional_fields

        if update_optional_fields is not None:
            self.update_optional_fields = update_optional_fields

    def create(self, element, collection_name=None):
        alt_colname(self, collection_name)

        # Validator will throw error if invalid
        self.validator.validate(element, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(element, self.collection_name)
        return "Inserted _Id : " + res

    def find(self, element, nowpage, collection_name=None):
        alt_colname(self, collection_name)
        self.pagination.tot_pagination(nowpage, self.collection_name)

        result = {
            'list': self.db.find(element, self.collection_name, skip=(nowpage-1)*self.pagination.pagesize, limit=self.pagination.pagesize),
            'pagination': self.pagination
        }
        return result

    def find_by_id(self, id, collection_name=None):
        alt_colname(self, collection_name)
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, element, collection_name=None):
        alt_colname(self, collection_name)

        self.validator.validate(element, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, element, self.collection_name)

    def delete(self, id, collection_name=None):
        alt_colname(self, collection_name)
        return self.db.delete(id, self.collection_name)

def alt_colname(object, colname):
    if colname is not None:
        object.collection_name = colname




