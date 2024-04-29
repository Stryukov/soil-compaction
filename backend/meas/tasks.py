import logging

from celery import shared_task


logger = logging.getLogger(__name__)

@shared_task
def create_protocol(measurement_id):
    from meas.models import Measurement

    measurement = Measurement.objects.get(pk=measurement_id)
    logger.info(measurement)
