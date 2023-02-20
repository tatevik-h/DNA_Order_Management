import celery as Celery
from celery import shared_task
from datetime import datetime, timedelta
from .models import DNASynthesisOrder
from django.conf import settings

@shared_task
def move_approved_orders_to_in_production():
    approved_orders = DNASynthesisOrder.objects.filter(status='complete')
    for order in approved_orders:
        order.status = 'in-production'
        order.save()


app = Celery('myapp')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'move_approved_orders_to_in_production': {
        'task': 'orders.tasks.move_approved_orders_to_in_production',
        'schedule': timedelta(minutes=5),
    },
}

