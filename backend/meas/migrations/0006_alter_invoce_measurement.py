# Generated by Django 5.0.4 on 2024-04-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0005_devicereadings_compaction_ratio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoce',
            name='measurement',
            field=models.ManyToManyField(to='meas.measurement', verbose_name='Измерения'),
        ),
    ]