from abc import ABC, abstractmethod

from flask import Flask

from iabot.actions import FlaskEndPointAction


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
