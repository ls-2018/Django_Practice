import six
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

INSTALLED_APPS += [
    'debug_toolbar',
    'djdt_flamegraph',
    'pympler',
    'debug_toolbar_line_profiler',
    'silk',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1', ]
SILKY_PYTHON_PROFILER = True

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',

    # Toolbar options
    'DISABLE_PANELS': {'debug_toolbar.panels.redirects.RedirectsPanel'},
    'INSERT_BEFORE': '</body>',
    'RENDER_PANELS': None,
    'RESULTS_CACHE_SIZE': 10,
    'ROOT_TAG_EXTRA_ATTRS': '',
    'SHOW_COLLAPSED': False,
    'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
    # Panel options
    'EXTRA_SIGNALS': [],
    'ENABLE_STACKTRACES': True,
    'HIDE_IN_STACKTRACES': (
        'socketserver' if six.PY3 else 'SocketServer',
        'threading',
        'wsgiref',
        'debug_toolbar',
        'django',
    ),
    'PROFILER_MAX_DEPTH': 10,
    'SHOW_TEMPLATE_CONTEXT': True,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
    ),
    'SQL_WARNING_THRESHOLD': 500,  # milliseconds
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'debug.log',
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'brief',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

DEBUG_TOOLBAR_PANELS = [
    # debug_toolbar自带
    # 'debug_toolbar.panels.versions.VersionsPanel',
    # 'debug_toolbar.panels.timer.TimerPanel',
    # 'debug_toolbar.panels.settings.SettingsPanel',
    # 'debug_toolbar.panels.headers.HeadersPanel',
    # 'debug_toolbar.panels.request.RequestPanel',
    # 'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 'debug_toolbar.panels.templates.TemplatesPanel',
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',

    # 'djdt_flamegraph.FlamegraphPanel',  # 火焰图    ,windows有问题 attribute 'SIGALRM'

    # 'pympler.panels.MemoryPanel',  # 内存占用分析

    'debug_toolbar_line_profiler.panel.ProfilingPanel',  # 行级性能分析插件

]
