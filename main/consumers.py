import json 
from channels.generic.websocket import WebsocketConsumer
from main.models import Game
from datetime import datetime
from asgiref.sync import async_to_sync


class ChessConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        try:
            last_room = Game.objects.latest('created')
            if not last_room.join(self.user):
                new_room = self.createRoom()
                self.room = str(new_room.id)
            else:
                self.room = str(last_room.id)

        except Game.DoesNotExist:
            new_room = self.createRoom()
            self.room = str(new_room.id)

        self.accept()

        self.send(text_data=json.dumps({
            "room": str(self.room)
        }))
        
        async_to_sync(self.channel_layer.group_add)(
            self.room, self.channel_name
        )
   
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room, self.channel_name
        )

    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def createRoom(self):
        new_room = Game.objects.create()
        new_room.join(self.user)
        return new_room