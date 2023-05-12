from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("elec/", include('ElectricityBills.urls')),
    path("gas/", include('GasBills.urls')),
    path("buildings/", include('Buildings.urls')),
    path("water/", include('WaterBills.urls')),
    path("service/",views.service,name='service'),
    path("index/",views.index,name='index'),
    path("contact/",views.contact,name='contact'),
    path("about/",views.about,name='about'),
]
