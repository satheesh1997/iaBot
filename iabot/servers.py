from abc import ABC, abstractmethod

from flask import Flask

from iabot.actions import FlaskEndPointAction

import asyncio
import websockets
import json


class AbstractServer(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass


class HTTPServer(AbstractServer):
    def __init__(self, bot, name="iaBot", port=8000):
        self.app = Flask(name)
        self.bot = bot
        self.port = port
        self.app.add_url_rule(
            "/",
            "iabot-endpoint",
            FlaskEndPointAction(self.bot.on_message),
            methods=["POST"],
        )

    def run(self):
        self.app.run(port=self.port)


class WebsocketServer(AbstractServer):
    def __init__(self, bot, port=8000):
        self.server = websockets.serve(self.echo, "localhost", port)
        self.bot = bot

    async def echo(self, websocket, path):
        async for message in websocket:
            await websocket.send(json.dumps(self.bot.on_message(json.loads(message))))

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()
