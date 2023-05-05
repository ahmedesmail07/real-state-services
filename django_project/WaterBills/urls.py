from django.urls import path, include
from . import views
urlpatterns = [
    path("9", views.form_nine, name="form-six"),
    path("10", views.form_ten, name="form-ten"),
    path("11", views.form_eleven, name="form-eleven"),

]
