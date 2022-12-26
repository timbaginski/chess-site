import json 
from channels.generic.websocket import WebsocketConsumer
from main.models import Game
from datetime import datetime


class ChessConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope['user']
        try:
            last_room = Game.objects.latest('created')
            if not last_room.join(self.user):
                new_room = self.createRoom()
                self.room = new_room
            else:
                self.room = last_room

        except Game.DoesNotExist:
            new_room = self.createRoom()
            self.room = new_room

        self.send(text_data=json.dumps({
            "room": str(self.room.id)
        }))
   
    def disconnect(self, close_code):
        pass

    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))

    def createRoom(self):
        new_room = Game.objects.create()
        new_room.join(self.user)
        return new_room