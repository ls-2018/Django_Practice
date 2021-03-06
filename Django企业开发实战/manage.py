#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # 设定Django的settings模块。
    # 通过读取系统环境变量中的  TYPEIDEA_PROFILE    来控制Django加载不同的配置文件
    profile = os.environ.get("TYPEIDEA_PROFILE", "develop")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django企业开发实战.settings.%s" % profile)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
