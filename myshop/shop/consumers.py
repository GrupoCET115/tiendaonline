from datetime import datetime
import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import FeedbackShop

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        # accept connection
        self.accept()
    def disconnect(self, close_code):
        pass
        # receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = datetime.now()
        # guardar feedback
        usuario = User.objects.get(username=self.user)
        feedback = FeedbackShop(usuario=usuario, mensaje=message)
        feedback.save()

        # send message to WebSocket
        self.send(text_data=json.dumps({'message': message, 'datetime': now.isoformat(), 'user': str(self.user)}))