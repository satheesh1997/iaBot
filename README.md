# iaBot

iaBot is a Python library for creating simple bots and serving it with the different ways available.


[![PyPI version](https://badge.fury.io/py/iaBot.svg)](https://badge.fury.io/py/iaBot)




## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install iaBot
```

## A simple bot

```python
from iabot import CreateBot
from iabot.handlers import SystemInformationHandler
from iabot.servers import HttpServer

handlers = [
   SystemInformationHandler
]
bot = CreateBot(
   handlers=handlers
)
bot_server = HttpServer(bot)
bot_server.run()
```

This creates a simple bot that will be listening to HttpRequests on the port 8000. Using any tool available send a post request to http://<your_domain.com>:8000/ with the following data.
```json
{
  "handler": "system",
  "action": "time"
}

```
On successfull request you will get time in the response as json.

### Handlers
These are used to group a set of similar actions. You can create your own handlers by inheriting the base handler.
```python
from iabot.handlers import BaseHandler

class StockHandler(BaseHandler):
    handle = 'stock'

    def get_stocks(self, *args, **kwargs):
      .....
      ....

```

Once you create a handler with the actions you can register it to a bot by adding the handler to the list of handlers.

### Actions
These are functions that a bot can execute to do the job when asked for. In the above StockHandler, get_stocks is an action. The response of all the actions should be a dictionary.

When a request reaches the server it will execute the particular action inside the handler. You can also send some additional data to your actions by passing it as a dict using data key in the request data. Remember a handler should always return a dict.

```json
{
  "handler": "stock",
  "action": "get_stocks",
  "data": {
     "date": "04-5-2010"
   }
}

```

Will be updating more and adding more type of servers to serve the bot.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
