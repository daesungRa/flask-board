import os
from werkzeug.utils import secure_filename

class Profile_Upload(object):
    def upload(self, instance_path, profile):
        try:
            profile_name = secure_filename(profile.filename)
            savepath = os.path.join(instance_path.split('instance')[0], 'src', 'static', 'imgs', 'members', profile_name)
            if os.path.exists(savepath):
                import secrets
                savepath = savepath.split('.')[0] + secrets.token_hex(16) + '.' + savepath.split('.')[1]
            print('실제 파일 저장경로 : ' + savepath)
            profile.save(savepath)

            savepath = savepath.split('flask-board\\')[1]
            return savepath
        except:
            print('raise exception during file upload..')
            return None