import json 
from channels.generic.websocket import WebSocketConsumer

class ChessConsumer(WebSocketConsumer):
    def connect(self):
        self.accept()
        
        self.send(text_data=json.dumps({
            'type': 'connection has been established',
            'message': 'you are connected'
        }))