from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('form1/',views.provideElectricMeter,name='form1'),
    path('form2/',views.form2,name='form2'),

]

