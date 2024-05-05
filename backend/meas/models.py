from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from meas.tasks import create_protocol


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
    mark = models.CharField('Маркировка', max_length=10)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        related_name='customer',
        null=True,
        blank=True
    )

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
    tag_number = models.CharField('Номер метки', max_length=20)
    blow_number = models.CharField('Номер удара', max_length=20)
    created_at = models.DateField('Дата измерений')
    elastic_modulus = models.PositiveSmallIntegerField(
        'Модуль упругости, F, MH/м.кв'
    )
    movement = models.PositiveSmallIntegerField('Перемещение L, мкм')
    power_of_blow = models.PositiveSmallIntegerField('Сила Удара Fmax, H')
    compaction_ratio = models.CharField(
        'Коэффециент уплотнения', max_length=20
    )
    device_type = models.CharField(
        'Тип устройства',
        max_length=100,
        default='Измеритель модуля упругости грунтов и основания дорог ПДУ-МГ4'
    )
    measurement = models.ForeignKey(
        'Measurement', on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Данные с устройства'
        verbose_name_plural = 'Данные с устройства'
        ordering = ['-created_at']

    def __str__(self):
        return f'Удар №{self.blow_number} {self.created_at}'


class Measurement(models.Model):
    visited_at = models.DateField('Дата выезда')
    testing_location = models.ForeignKey(
        TestingLocation,
        on_delete=models.CASCADE,
        verbose_name='Место испытаний'
    )
    layer = models.CharField('Слой', max_length=50)
    material = models.CharField('Материал', max_length=50)
    create_docs = models.BooleanField('Созданы документы')
    protocol = models.FileField(
        'Протокол', upload_to='docs/protocol/%Y/%m/%d', null=True, blank=True
    )
    work_request = models.FileField(
        'Заявка', upload_to='docs/request/%Y/%m/%d', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Измерения'
        verbose_name_plural = 'Измерения'
        ordering = ['-visited_at']

    def __str__(self):
        return f'{self.testing_location} ({self.visited_at})'


@receiver(post_save, sender=Measurement)
def create_docs(sender, instance, created, **kwargs):
    if instance.create_docs and not instance.protocol:
        create_protocol.delay_on_commit(instance.pk)


class Invoce(models.Model):
    number = models.CharField('Номер счета', max_length=20)
    billed_at = models.DateField('Дата счета')
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, verbose_name='Заказчик'
    )
    measurement = models.ManyToManyField(Measurement, verbose_name='Измерения')
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
