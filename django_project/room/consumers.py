import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required
from .models import Room
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # get the user's username address from the request
        username = self.scope["user"].username

        # use the username address as the room name
        self.room_group_name = f"room_{username}"

        # look up the room in the database
        try:
            room = Room.objects.get(name=username)
        except Room.DoesNotExist:
            # if the room doesn't exist, return an error message
            self.close(code=4404)
            return

        # join the room's channel group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        print(self.room_group_name)
        # accept the WebSocket connection
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
