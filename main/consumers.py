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
            "type": "join_notification",
            "room": str(self.room)
        }))
        
        async_to_sync(self.channel_layer.group_add)(
            self.room, self.channel_name
        )

        self.sendUpdatedRoom()

        
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room, self.channel_name
        )

        if self.room != None:
            rooms = Game.objects.filter(id=self.room)
            rooms[0].removePlayer(self.user)


    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        move = text_data_json["fen"]
        
        self.sendUpdatedRoom()

    def createRoom(self):
        new_room = Game.objects.create()
        new_room.join(self.user)
        return new_room

    def sendUpdatedRoom(self):
        rooms = Game.objects.filter(id=self.room)
        room = list(rooms)[0]
        if room.inProgress():
            async_to_sync(self.channel_layer.group_send)(
                self.room, {"type": "state_notification", "fen": room.fen}
            )

    def state_notification(self, event):
        self.send(text_data=json.dumps(event))
   