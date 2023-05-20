from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ProvideGasMeterView(generics.CreateAPIView):
    queryset = ProvideGasMeter.objects.all()
    serializer_class = ProvideGasMeterSerializer
    permission_classes = [AllowAny]

class NaturalGasReadingView(generics.CreateAPIView):
    queryset = NaturalGasReading.objects.all()
    serializer_class = NaturalGasReadingSerializer
    permission_classes = [AllowAny]
    
class CollectingGasBillsView(generics.CreateAPIView):
    queryset = CollectingGasBills.objects.all()
    serializer_class = CollectingGasBillsSerializer
    permission_classes = [AllowAny]


