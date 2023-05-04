from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("electricity/", include('ElectricityBills.urls')),
    path("gas/", include('GasBills.urls'))
]
