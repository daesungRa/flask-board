from src.factory.validation import Validator
from src.factory.database import Database

class Member_service(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.collection_name = 'members'
        self.fields = {
            'username': 'string',
            'pwd': 'string',
            'email': 'string',
            'nickname': 'string',
            'profile': 'string',
            'auth': 'int',
            'created': 'datetime'
        }
        self.create_required_fields = ['username', 'pwd', 'email', 'auth']
        self.create_optional_fields = []
        self.update_required_fields = ['pwd']
        self.update_optional_fields = []
    
    def create_account(self, form):
        # 이메일(아이디)이 같다면 1, 닉네임(유니크)이 같다면 2 플래그 반환
        # 3 번 플래그는 성공, 플래그에 따라 응답 다르게
        pass
    
    def find_account(self, form):
        # 이메일(아이디)이 다르다면 1, 비밀번호가 다르다면 2 플래그 반환
        # 3 번 플래그는 성공(+세션에 저장할 정보), 플래그에 따라 응답 다르게
        pass
    
    def modify_account(self, form):
        pass

    def delete_account(self, form):
        pass

    def signin(self, form):
        pass