from rest_framework import serializers
from .models import *

class ProvideGasMeterSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProvideGasMeter
        fields = '__all__'

class NaturalGasReadingSerializer(serializers.ModelSerializer):
    class Meta :
        model = NaturalGasReading
        fields = '__all__'

class CollectingGasBillsSerializer(serializers.ModelSerializer):
    class Meta :
        model = CollectingGasBills
        fields = '__all__'