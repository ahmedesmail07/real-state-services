import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'room_{self.room_name}'

        # look up the room in the database
        try:
            room = Room.objects.get(name=self.room_name)
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
        print(text_data_json)
        username = text_data_json['username']
        room = text_data_json['room']

        self.save_message(username,room,message)
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':message,
                'username':username
            }
        )

    def chat_message(self,event):
        message = event['message']
        username = event['username']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username':username
        }))
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)
