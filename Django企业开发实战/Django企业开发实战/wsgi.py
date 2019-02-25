"""
WSGI.md config for Django企业开发实战 project.

It exposes the WSGI.md callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 设定Django的settings模块。
# 通过读取系统环境变量中的  TYPEIDEA_PROFILE    来控制Django加载不同的配置文件
profile = os.environ.get("TYPEIDEA_PROFILE", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django企业开发实战.settings.%s" % profile)

application = get_wsgi_application()
