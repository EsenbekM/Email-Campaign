from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_campaign.settings.base')

app = Celery('email_campaign')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-daily-campaign-statistics': {
        'task': 'campaigns.tasks.send_daily_campaign_statistics',
        'schedule': crontab(hour=0, minute=0),  # Запуск каждый день в полночь
    },
}