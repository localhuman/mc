__author__ = 'thomassaunders'

import os
import sys

path='/var/www/html/mcdjango'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE']='moderncarpentry.settings_live'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()