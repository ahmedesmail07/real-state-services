from django.contrib import admin
<<<<<<< HEAD
from .models import ProvideGasMeter, NaturalGasReading

admin.site.register(ProvideGasMeter)

admin.site.register(NaturalGasReading)
=======
from .models import ProvideGasMeter, NaturalGasReading, CollectingGasBills

admin.site.register(ProvideGasMeter)
admin.site.register(NaturalGasReading)
admin.site.register(CollectingGasBills)
>>>>>>> 9dcf350bc7dfcb42091b1273627e8cf2c354ccb0
