import os
import logging

from django.db import transaction
from django.core.files.base import File

from celery import shared_task
from docxtpl import DocxTemplate


logger = logging.getLogger(__name__)


LABELS = {
    'elastic_modulus': 'Модуль упругости, F, МН/м.кв',
    'movement': 'Перемещение L, мкм',
    'power_of_blow': 'Сила Удара Fmax, H',
}


@shared_task
def create_protocol(measurement_id):
    from meas.models import Measurement, DeviceReadings

    with transaction.atomic():
        measurement = Measurement.objects.select_for_update().get(
            pk=measurement_id
        )

        context = {
            'col_labels': ['1-й удар', '2-й удар', '3-й удар', 'Среднее'],
            'tbl_contents': []
        }

        context['protocol_number'] = '-'.join([
            measurement.testing_location.area.mark,
            str(measurement.visited_at.day),
            str(measurement.visited_at.month)
        ])
        context['protocol_date'] = measurement.visited_at
        context['customer_name'] = measurement.testing_location.area.customer.name
        context['area_name'] = measurement.testing_location.area.name
        context['location_name'] = measurement.testing_location.name
        context['material'] = measurement.material
        context['testing_date'] = measurement.visited_at
        context['request_number'] = context['protocol_number'] + ' от ' + str(context['protocol_date'])

        tags = DeviceReadings.objects.filter(measurement=measurement).values_list('tag_number', flat=True).distinct()
        for tag in tags:
            tag_readings = DeviceReadings.objects.filter(measurement=measurement, tag_number=tag).select_for_update()

            ratio = tag_readings.values_list('compaction_ratio', flat=True).first()
            data_for_tag = {
                'tag': 'Отметка ' + tag,
                'ratio': ratio,
                'data': []
            }

            # Создаем данные для каждого измерения
            for field in ['elastic_modulus', 'movement', 'power_of_blow']:
                values = tag_readings.values_list(field, flat=True)
                average = round(sum(values) / len(values))
                data_for_tag['data'].append({
                    'label': LABELS[field],
                    'cols': [str(value) for value in values] + [str(average)]
                })
            context['tbl_contents'].append(data_for_tag)

        path_output_file = './tpls/generated_protocol.docx'
        doc = DocxTemplate("./tpls/protocol_tpl.docx")
        doc.render(context)
        doc.save(path_output_file)
        # there need convert to pdf
        with open(path_output_file, 'rb') as f:
            measurement.protocol.save(f'protocol_{measurement_id}.docx', File(f))
    os.remove(path_output_file)
