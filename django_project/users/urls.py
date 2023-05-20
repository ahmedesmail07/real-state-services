from django.urls import include, path
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('logout/', LogoutUser, name='logout'),
]

