from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Room
from django.shortcuts import get_object_or_404, render
# Create your views here.
{login_required}
def room(request,slug):
    room = Room.objects.get(slug = slug)
    return render(request, 'room/room.html', {'room': room})

{login_required}
def profile(request):
    return render(request, 'room/user.html', {'user': request.user})

@user_passes_test(lambda user:user.is_superuser)
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


