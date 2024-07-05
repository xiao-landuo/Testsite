# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')

# app = Celery('mysite')
# app.config_from_object('django.conf:settings')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')

app = Celery('mysite')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)