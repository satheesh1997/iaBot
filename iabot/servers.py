from abc import ABC, abstractmethod
import asyncio
import json
import signal
import websockets

from flask import Flask

from iabot.actions import FlaskEndPointAction
from iabot.constants import ACTION_ERROR


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
        self.bot = bot
        self.loop = asyncio.get_event_loop()
        self.port = port

    async def create_server(self, stop):
        async with websockets.serve(self.echo, "0.0.0.0", self.port):
            await stop

    async def echo(self, websocket):
        async for message in websocket:
            try:
                response_load = self.bot.on_message(json.loads(message))
            except json.decoder.JSONDecodeError as e:
                response_load = {"status": ACTION_ERROR, "message": str(e)}
            await websocket.send(json.dumps(response_load))

    def run(self):
        stop = self.loop.create_future()
        try:
            self.loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)
        except NotImplementedError:
            pass
        self.loop.run_until_complete(self.create_server(stop))
