import os
import sys	
sys.path.append('/var/www/mailinator/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mailinator.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
