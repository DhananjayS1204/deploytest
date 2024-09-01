# DeployModel/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Ensure this matches your settings module's location
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeployModel.settings')

application = get_wsgi_application()
