from flask_bcrypt import Bcrypt

class Encryption(object):
    def __init__(self):
        self.bcrypt = Bcrypt()

    def hash_pwd(self, pwd: str):
        return self.bcrypt.generate_password_hash(pwd).decode('utf-8')

    def check_pwd(self, saved_pwd: str, inserted_pwd: str):
        return self.bcrypt.check_password_hash(saved_pwd, inserted_pwd)



