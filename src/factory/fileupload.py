import os
from werkzeug.utils import secure_filename

class Profile_Upload(object):
    def upload(self, instance_path, profile):
        try:
            profile_name = secure_filename(profile.filename)
            savepath = os.path.join(instance_path.split('instance')[0], 'static', 'imgs', 'members', profile_name)
            if os.path.exists(savepath):
                import secrets
                savepath = savepath.split('.')[0] + secrets.token_hex(16) + '.' + savepath.split('.')[1]
            profile.save(savepath)

            savepath = savepath.split('src')[1]
            return savepath
        except:
            print('raise exception during file upload..')
            return None