import os
import sys
sys.path.append('/var/www/mailinator/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mailinator.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
