from rest_framework import serializers
from .models import Payment,MeterRequest, PayBills, LicenseRequest, ReconciliationRequest

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class MeterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterRequest
        fields = '__all__'


class PayBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayBills
        fields = '__all__'


class LicenseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseRequest
        fields = '__all__'


class ReconciliationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReconciliationRequest
        fields = '__all__'
