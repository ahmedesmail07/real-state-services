from django.urls import path, include
from . import views
urlpatterns = [
    path("6", views.form_six, name="form-six"),
    path("7", views.form_seven, name="form-seven")
]
