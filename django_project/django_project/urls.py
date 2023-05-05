from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("elec/", include('ElectricityBills.urls')),
    path("gas/", include('GasBills.urls')),
    path("buildings/", include('Buildings.urls')),
    path("water/", include('WaterBills.urls'))
]
