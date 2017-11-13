
from .base import *

config_secret = json.loads(open(CONFIG_SECRET_DEV_FILE).read())

# AWS
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.yabi.kr',
]

# AWS Storage
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# Databases
DATABASES = config_secret['django']['databases']

# FACEBOOK
FACEBOOK_APP_ID = config_secret['facebook']['app_id']
FACEBOOK_APP_SECRET_CODE = config_secret['facebook']['secret_code']
FACEBOOK_SCOPE = [
    'user_friends',
    'public_profile',
    'email',
]
