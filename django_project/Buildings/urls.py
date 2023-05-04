from django.urls import path, include
from . import views
urlpatterns = [
    path("12", views.form_twelve, name="form-twelve"),
    path("13", views.form_thirteen, name="form-thirteen"),


]
