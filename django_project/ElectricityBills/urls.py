from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('1/',views.provideElectricMeter,name='form1'),
    path('2/',views.form2,name='form2'),
    path('3/',views.form3,name='form3'),
    path('4/',views.form4,name='form4'),
    path('5/',views.form5,name='form5'),

]

