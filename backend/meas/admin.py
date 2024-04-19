from django.contrib import admin

from .models import Customer, Area, TestingLocation, DeviceReadings, Measurement, Invoce


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)


@admin.register(TestingLocation)
class TestingLocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'area',
    )
    search_fields = ('name','area__name')
    list_filter = ('area',)


@admin.register(DeviceReadings)
class DeviceReadingsAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'blow_number',
        'elastic_modulus',
        'movement',
        'power_of_blow',
        'device_type',
    )
    list_filter = ('created_at',)
    search_fields = ('created_at',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = (
        'visited_at',
        'testing_location',
        'layer',
        'material',
        'device_readings',
    )
    search_fields = ('testing_location',)
    list_filter = ('visited_at',)


class Measurementinline(admin.TabularInline):
    model = Measurement
    extra = 1


@admin.register(Invoce)
class InvoceAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'billed_at',
        'status',
    )
    list_filter = ('status', 'billed_at')
    list_editable = ('status',)
    inlines = [Measurementinline,]
