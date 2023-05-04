from django.contrib import admin
from .models import ProvideGasMeter, NaturalGasReading, CollectingGasBills

admin.site.register(ProvideGasMeter)
admin.site.register(NaturalGasReading)
admin.site.register(CollectingGasBills)