# Generated by Django 4.2.11 on 2024-04-14 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя заказчика')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceReadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blow_number', models.CharField(max_length=20, verbose_name='Номер удара')),
                ('elastic_modulus', models.PositiveSmallIntegerField(verbose_name='Модуль упругости, F, MH/м.кв')),
                ('movement', models.PositiveSmallIntegerField(verbose_name='Перемещение L, мкм')),
                ('power_of_blow', models.PositiveSmallIntegerField(verbose_name='Сила Удара Fmax, H')),
                ('device_type', models.CharField(default='Измеритель модуля упругости грунтов и основания дорог ПДУ-МГ4', max_length=100, verbose_name='Тип устройства')),
            ],
        ),
        migrations.CreateModel(
            name='TestingLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='meas.area')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_at', models.DateField(auto_now_add=True, verbose_name='Дата выезда')),
                ('layer', models.CharField(max_length=50, verbose_name='Слой')),
                ('material', models.CharField(max_length=50, verbose_name='Материал')),
                ('device_readings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_readings', to='meas.devicereadings')),
                ('testing_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meas.testinglocation', verbose_name='Место испытаний')),
            ],
        ),
        migrations.CreateModel(
            name='Invoce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер счета')),
                ('billed_at', models.DateField(auto_now_add=True, verbose_name='Дата счета')),
                ('status', models.CharField(choices=[('NEW', 'Создан'), ('SENT', 'Выставлен'), ('PAID', 'Оплачен')], default=('NEW', 'Создан'), max_length=10, verbose_name='Статус')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='measurements', to='meas.measurement')),
            ],
        ),
    ]
