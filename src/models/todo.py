from src.factory.validation import Validator
from src.factory.database import Database

class Todo(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = 'todos' # collection name

        self.fields = {
            "title": "string",
            "body": "string",
            "created": "datetime",
            "updated": "datetime",
        }

        self.create_required_fields = ["title", "body"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = ["title", "body"]

        # Fields optional for UPDATE
        self.update_optional_fields = []

    def create(self, todo):
        # Validator will throw error if invalid
        self.validator.validate(todo, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(todo, self.collection_name)
        return "Inserted _Id " + res

    def find(self, todo, collection_name=None):
        # 컬렉션 변경 가능하도록 수정 (190517, fri)
        ## 'Todo' 인 클래스명도 변경 요망
        if collection_name is not None:
            self.collection_name = collection_name
        return self.db.find(todo, self.collection_name)

    def find_by_id(self, id, collection_name=None):
        # 컬렉션 변경 가능하도록 수정 (190517, fri)
        ## 'Todo' 인 클래스명도 변경 요망
        if collection_name is not None:
            self.collection_name = collection_name
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, todo):
        self.validator.validate(todo, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, todo, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)






