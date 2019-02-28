# coding:utf-8
from setuptools import setup, find_packages

setup(
    name='Django企业开发实战',
    version='${version}',
    description='Blog System base on Django',
    author='ls',
    author_email='1214972346@qq.com',
    url='https://www.shuoiliu.com',
    license='MIT',
    packages=find_packages('Django企业开发实战'),
    package_dir={'': 'Django企业开发实战'},
    # package_data={'': [    # 打包数据文件，方法一
    # 'static/*/*',  # 需要按目录层级匹配
    # ]},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'django_autocomplete_light==3.2.10',
        'six == 1.11.0',
        'Django == 2.0.1',
        'xadmin == 2.0.1',
        'Markdown == 3.0.1',
        'mistune == 0.8.4',
        'django_ckeditor == 5.6.1',
        'Pillow == 4.0.0',
        'dal == 0.2',
        'djangorestframework == 3.9.1',
        # cache
        'django-redis==4.10.0',
        'hiredis==1.0.0',
        # debug
        'django-debug-toolbar==1.9.1',
        'django_silk == 3.0.0',
        'silk == 0.1',
    ],
    extras_require={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'Django企业开发实战/manage.py',
        'Django企业开发实战/Django企业开发实战/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'Django企业开发实战_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # 软件成熟度如何？
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 指明项目的受众
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # 选择项目的许可证
        'License :: OSI Approved :: MIT License',

        # 指定项目需要使用的python版本
        'Programming Language :: Python :: 3.6',
    ],

)
