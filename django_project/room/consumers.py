import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required
from .models import Room
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):

    async def connect(self):
        # get the user's username address from the request
        username = self.scope["user"].username

        # use the username address as the room name
        self.room_group_name = f"room_{username}"

        # check if the room already exists in the database
        try:
            room = Room.objects.get(name=username)
        except Room.DoesNotExist:
            # create a new Room object and save it to the database
            room = Room(name=username)
            room.save()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_group_name)
        print("using the defulat conntect")
        self.accept()
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':message
            }
        )

    def chat_message(self,event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
