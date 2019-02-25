from .base import *  # N0QA

# flake8: N0QA
DEBUG = True


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
