from src.factory.validation import Validator
from src.factory.database import Database
from src.factory.fileupload import Profile_Upload
import os

class Member_service(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.profile_upload = Profile_Upload()
        self.collection_name = 'members'
        self.fields = {
            'email': 'string',
            'username': 'string',
            'nickname': 'string',
            'pwd': 'string',
            'profile': 'string',
            'auth': 'int',
            'created': 'datetime'
        }
        self.create_required_fields = ['email', 'username', 'pwd', 'auth']
        self.create_optional_fields = ['nickname', 'profile', 'created']
        self.update_required_fields = ['email', 'pwd']
        self.update_optional_fields = ['username', 'nickname', 'profile', 'created']

    def create_account(self, instance_path, form):
        ## duplicated file check and save
        savepath = self.profile_upload.upload(instance_path, form.profile.data)

        if savepath:
            element = {
                'email': form.email.data,
                'username': form.username.data,
                'nickname': form.nickname.data,
                'pwd': form.pwd.data,
                'profile': savepath,
                'auth': 1
            }

            ## register user info to database
            self.validator.validate(element, self.fields, self.create_required_fields, self.create_optional_fields)
            result = self.db.insert(element, self.collection_name)

            if result != 'duplicate key error':
                create_account_result = 1; # success
            elif result == 'duplicate key error':
                # remove saved file
                filename = instance_path.split('\instance')[0] + savepath
                os.remove(filename)

                create_account_result = 3; # duplicate key error
            else:
                create_account_result = 4;  # database error
        else:
            create_account_result = 2; # fail for file save

        return create_account_result

    def access_account(self, form):
        criteria = {
            'email': form.email.data,
            'pwd': form.pwd.data
        }
        find_result = self.db.find(criteria, self.collection_name, projection=['email', 'nickname'])

        return find_result

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