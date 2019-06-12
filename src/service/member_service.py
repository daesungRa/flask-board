from src.factory.validation import Validator
from src.factory.database import Database
from src.factory.fileupload import Profile_Upload
from src.factory import encryption
import os

class Member_service(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.profile_upload = Profile_Upload()
        self.encryption_instance = encryption.Encryption()

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
        create_account_result = 2

        if savepath:
            element = {
                'email': form.email.data,
                'username': form.username.data,
                'nickname': form.nickname.data,
                'pwd': self.encryption_instance.hash_pwd(form.pwd.data),
                'profile': savepath,
                'auth': 1 # 1: common, 2: admin, 3: super_admin
            }

            ## register user info to database
            self.validator.validate(element, self.fields, self.create_required_fields, self.create_optional_fields)
            result = self.db.insert(element, self.collection_name)

            if result != 'duplicate key error':
                create_account_result = 1 # success
            elif result == 'duplicate key error':
                # remove saved file
                filename = instance_path.split('instance')[0] + savepath
                print(f'remove file name : {filename}')
                os.remove(filename)

                create_account_result = 3 # duplicate key error
            else:
                create_account_result = 4 # database error
        else:
            create_account_result = 2 # fail for file save

        return create_account_result

    def access_account(self, form):
        criteria = {'email': form.email.data}
        saved_result = self.db.find_one(criteria, self.collection_name, projection=['email', 'pwd', 'nickname', 'profile'])

        if saved_result:
            result = self.encryption_instance.check_pwd(saved_result['pwd'], form.pwd.data)

            if result:
                saved_result.pop('pwd')
                return saved_result
        return None

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