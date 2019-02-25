import os

from .base import *  # N0QA

"""
# N0QA  告诉PEP8 检测工具，这个地方不需要检测
# flake8: N0QA  文件第一行，这个文件不用检测
"""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
