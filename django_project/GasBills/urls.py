from django.urls import path, include
from . import views
urlpatterns = [
    path("6", views.form_six, name="form-six"),
<<<<<<< HEAD
    path("7", views.form_seven, name="form-seven")
=======
    path("7", views.form_seven, name="form-seven"),
    path("8", views.form_eight, name="form-eight"),
>>>>>>> 9dcf350bc7dfcb42091b1273627e8cf2c354ccb0
]
