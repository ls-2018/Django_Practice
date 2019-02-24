"""
WSGI.md config for Django企业开发实战 project.

It exposes the WSGI.md callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django企业开发实战.settings")

application = get_wsgi_application()
