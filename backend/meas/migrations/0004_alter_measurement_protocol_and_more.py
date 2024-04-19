# Generated by Django 5.0.4 on 2024-04-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0003_invoce_customer_measurement_create_docs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='protocol',
            field=models.FileField(blank=True, null=True, upload_to='docs/protocol/%Y/%m/%d', verbose_name='Протокол'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='work_request',
            field=models.FileField(blank=True, null=True, upload_to='docs/request/%Y/%m/%d', verbose_name='Заявка'),
        ),
    ]
