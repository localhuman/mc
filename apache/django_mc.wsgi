__author__ = 'thomassaunders'

import os
import sys

path='/var/www/html/mcdjango'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE']='moderncarpentry.settings_live'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()