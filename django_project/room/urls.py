from django.urls import path
from . import views
urlpatterns = [
    path('<slug:slug>/',views.room,name="room"),
    path('rooms',views.rooms,name="rooms"),
    path('', views.profile, name='profile'),
]
