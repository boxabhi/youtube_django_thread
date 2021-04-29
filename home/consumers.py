from channels.generic.websocket import AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync,sync_to_async
import json


class StateProgress(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'order'
        self.room_group_name = 'order'
        print(self.room_group_name)
        
        await (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        await self.send(text_data=json.dumps({
            'payload': "connected"
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'order_status',
                'payload': text_data
            }
        )

    # Receive message from room group
    async def order_status(self, event):
        #print(event)
        data = json.loads(event['value'])
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'payload': data
        }))