from django.db import models


INVOCE_STATUS_CHOICES = (
    ("NEW", "Создан"),
    ("SENT", "Выставлен"),
    ("PAID", "Оплачен"),
)


class Customer(models.Model):
    name = models.CharField('Имя заказчика', max_length=100)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['name']

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField('Наименование', max_length=100)

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'
        ordering = ['name']

    def __str__(self):
        return self.name


class TestingLocation(models.Model):
    name = models.CharField('Наименование', max_length=100)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='area'
    )

    class Meta:
        verbose_name = 'Место испытаний'
        verbose_name_plural = 'Места испытаний'
        ordering = ['name']

    def __str__(self):
        return self.name


class DeviceReadings(models.Model):
    blow_number = models.CharField('Номер удара', max_length=20)
    created_at = models.DateField('Дата измерений')
    elastic_modulus = models.PositiveSmallIntegerField(
        'Модуль упругости, F, MH/м.кв'
    )
    movement = models.PositiveSmallIntegerField('Перемещение L, мкм')
    power_of_blow = models.PositiveSmallIntegerField('Сила Удара Fmax, H')
    device_type = models.CharField(
        'Тип устройства',
        max_length=100,
        default='Измеритель модуля упругости грунтов и основания дорог ПДУ-МГ4'
    )

    class Meta:
        verbose_name = 'Данные с устройства'
        verbose_name_plural = 'Данные с устройства'
        ordering = ['-created_at']

    def __str__(self):
        return f'Удар №{self.blow_number} {self.created_at}'


class Invoce(models.Model):
    number = models.CharField('Номер счета', max_length=20)
    billed_at = models.DateField('Дата счета')
    status = models.CharField(
        'Статус',
        choices=INVOCE_STATUS_CHOICES,
        max_length=10,
        default=INVOCE_STATUS_CHOICES[0]
    )

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ['-billed_at']

    def __str__(self):
        return f'Счет №{self.number}  от {self.billed_at}'


class Measurement(models.Model):
    visited_at = models.DateField('Дата выезда')
    testing_location = models.ForeignKey(
        TestingLocation,
        on_delete=models.CASCADE,
        verbose_name='Место испытаний'
    )
    invoce = models.ForeignKey(
        Invoce, on_delete=models.DO_NOTHING, related_name='invoce', null=True
    )
    layer = models.CharField('Слой', max_length=50)
    material = models.CharField('Материал', max_length=50)
    device_readings = models.ForeignKey(
        DeviceReadings,
        on_delete=models.CASCADE,
        related_name='device_readings',
        verbose_name='Данные с устройства',
    )

    class Meta:
        verbose_name = 'Измерения'
        verbose_name_plural = 'Измерения'
        ordering = ['-visited_at']

    def __str__(self):
        return f'{self.testing_location} ({self.visited_at})'