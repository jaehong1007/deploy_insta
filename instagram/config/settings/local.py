import random
import string

from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.yabi.kr',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = ''.join(
    [random.choice(string.ascii_lowercase) for i in range(40)]
)

config_secret = json.loads(open(CONFIG_SECRET_LOCAL_FILE).read())


# FACEBOOK
FACEBOOK_APP_ID = config_secret['facebook']['app_id']
FACEBOOK_APP_SECRET_CODE = config_secret['facebook']['secret_code']
FACEBOOK_SCOPE = [
    'user_friends',
    'public_profile',
    'email',
]
