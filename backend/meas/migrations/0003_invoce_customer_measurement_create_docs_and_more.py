# Generated by Django 5.0.4 on 2024-04-19 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0002_alter_area_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoce',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='meas.customer', verbose_name='Заказчик'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurement',
            name='create_docs',
            field=models.BooleanField(default=False, verbose_name='Создать протокол и заявку'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurement',
            name='protocol',
            field=models.FileField(blank=True, null=True, upload_to='protocol/%Y/%m/%d', verbose_name='Протокол'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='work_request',
            field=models.FileField(blank=True, null=True, upload_to='request/%Y/%m/%d', verbose_name='Заявка'),
        ),
    ]