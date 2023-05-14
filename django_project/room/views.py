from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Room
from django.shortcuts import get_object_or_404, render
# Create your views here.
{login_required}
def room(request):
   return  render(request,'room/room.html')

@user_passes_test(lambda user:user.is_superuser)
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


def join_room(request, room_slug):
    # get the room object from the database using the slug
    room = get_object_or_404(Room, slug=room_slug)

    # get the room name
    room_name = room.name

    # render the room template with the room object
    return render(request, 'room/admin_room.html', {'room': room, 'room_name': room_name})
