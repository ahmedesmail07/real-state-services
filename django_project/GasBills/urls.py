from django.urls import path, include
from . import views
from .api_views import *
urlpatterns = [
    path("6", views.form_six, name="form6"),
    path("7", views.form_seven, name="form7"),
    path("8", views.form_eight, name="form8"),
    path("api/6/",ProvideGasMeterView().as_view(),name="api_form6"),
    path("api/7/",NaturalGasReadingView().as_view(),name="api_form7"),
    path("api/8/",CollectingGasBillsView().as_view(),name="api_form8"),

]
