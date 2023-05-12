from django.urls import path, include
from . import views
urlpatterns = [
    path("6", views.form_six, name="form6"),
    path("7", views.form_seven, name="form7"),
    path("8", views.form_eight, name="form8"),

]
