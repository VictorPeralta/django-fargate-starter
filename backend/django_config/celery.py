import os

from celery import Celery, shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dango_config.settings')

celery_app = Celery('tasks')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')


celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'debug_task',
        'schedule': 30.0,
        'args': ()
    },
}



# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()

@shared_task(name="debug_task")
def debug_task():
    print('Request: test')
