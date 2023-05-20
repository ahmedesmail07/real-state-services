from rest_framework import serializers
from .models import *

class WaterMeterSerializer(serializers.ModelSerializer):
    class Meta :
        model = WaterMeter
        fields = '__all__'

class WaterMeterReadingSerializer(serializers.ModelSerializer):
    class Meta :
        model = WaterMeterReading
        fields = '__all__'

class CollectingWaterBillsSerializer(serializers.ModelSerializer):
    class Meta :
        model = CollectingWaterBills
        fields = '__all__'
