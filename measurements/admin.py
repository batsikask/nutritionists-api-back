from django.contrib import admin
from .models import BodyMeasurement, SegmentalBodyMeasurement, BiochemicalMeasurement, Diseases, Diet

admin.site.register(BodyMeasurement)
admin.site.register(SegmentalBodyMeasurement)
admin.site.register(BiochemicalMeasurement)
admin.site.register(Diseases)
admin.site.register(Diet)
