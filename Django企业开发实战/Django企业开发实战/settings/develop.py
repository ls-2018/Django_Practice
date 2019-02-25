from .base import *  # N0QA

# flake8: N0QA
# DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'localhost_test',
        'USER': 'root',
        'PASSWORD': '1234',
        "TEST": {
            'NAME': 'mytestsdatabase'
        }
    }
}
