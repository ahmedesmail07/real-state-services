from django.contrib import admin

from .models import CollectingWaterBills, WaterMeter, WaterMeterReading

admin.site.register(WaterMeter)
admin.site.register(WaterMeterReading)
admin.site.register(CollectingWaterBills)
