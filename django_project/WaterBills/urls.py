from django.urls import path, include
from . import views
urlpatterns = [
    path("9", views.form_nine, name="form9"),
    path("10", views.form_ten, name="form10"),
    path("11", views.form_eleven, name="form11"),

]
