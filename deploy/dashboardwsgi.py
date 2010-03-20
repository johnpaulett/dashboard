import site
import os
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
PY_VERSION = 'python%s' % (sys.version[0:3])

site.addsitedir(os.path.join(ROOT_DIR, 'env/lib/', PY_VERSION , 'site-packages'))
sys.path.append(os.path.join(ROOT_DIR, 'src'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

