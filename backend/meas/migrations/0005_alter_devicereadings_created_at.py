# Generated by Django 4.2.11 on 2024-04-19 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas', '0004_alter_devicereadings_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicereadings',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата измерений'),
        ),
    ]