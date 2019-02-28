from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',
        'USER': 'root',
        'PASSWORD': '1234',
        "TEST": {
            'NAME': 'mytestsdatabase'
        },
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

"""
    如果数据库中可能拥有类似emojj表情符号的字符，需要使用utf8mb4字符集，
    CONN_MAX_AGE    ：   连接存在的时间，django默认每来一个请求，都会创建一个新的数据库连接
    
    问题1：    数据库层抛出 too many connection
        ? 并发量过大来不及关闭连接时，导致连接数过大来不及关闭连接时，会导致连接数不断增加
    
    如果采用多线程的方式部署项目，最好不要配置CONN_MAX_AGE;因为如果每一新的请求来处理的话，那么每个持久化的连接就达不到复用的目的。
    
    gevent会给python的thread动态打补丁，导致数据库连接无法复用

"""
