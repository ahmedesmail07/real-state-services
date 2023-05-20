from rest_framework import serializers
from .models import BuildingPermitApplications,CollectingReconciliationBuilding

class BuildingPermitApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingPermitApplications
        fields = '__all__'

class CollectingReconciliationBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectingReconciliationBuilding
        fields = '__all__'