from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TokenAuthConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(self.scope["user"].username)
        print(self.scope["user"].email)

    async def disconnect(self, close_code):
        ...

    async def receive_json(self, message):
        command = message.get("command")
        if command == "Say hello !":
            print(message["data_string"])
            await self.send_json({
                "command_response": "The command to \
                say hello was received ",
                "data_string_bacK": message.get
              ("data_string", None)
            })
