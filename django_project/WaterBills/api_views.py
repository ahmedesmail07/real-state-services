from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny


class WaterMeterView(generics.CreateAPIView):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer
    permission_classes = [AllowAny]

class WaterMeterReadingView(generics.CreateAPIView):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterReadingSerializer
    permission_classes = [AllowAny]

class CollectingWaterBillsView(generics.CreateAPIView):
    queryset = WaterMeter.objects.all()
    serializer_class = CollectingWaterBillsSerializer
    permission_classes = [AllowAny]
