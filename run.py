import sys

from iabot import CreateBot
from iabot.handlers import SystemInformationHandler
from iabot.servers import HTTPServer


def start_http_server(bot):
    server = HTTPServer(bot)
    server.run()


if __name__ == "__main__":
    bot = CreateBot(handlers=[SystemInformationHandler])

    try:
        server_to_start = sys.argv[1]

        if server_to_start == "HTTP":
            start_http_server(bot)
    except IndexError:
        print("No server specified to run!")
        print("Servers:")
        print("* HTTP")
        print("* WS")
        print("* RPC")
        print("use python run.py <server>")
