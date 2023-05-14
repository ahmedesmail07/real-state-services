from django.urls import path
from . import views
urlpatterns = [
    path('',views.room,name="room"),
    path('rooms',views.rooms,name="rooms"),
    path('room/<slug:room_slug>/', views.join_room, name='join_room'),
]
