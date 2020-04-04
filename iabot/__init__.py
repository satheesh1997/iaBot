from iabot.handler import NotFound


class CreateBot(object):
    __handlers = {}

    def __init__(self, handlers):
        if not type(handlers) == "list":
            raise Exception("Handlers must be of type list")

        for handler in handlers:
            self.__register_handler(handler)

    def __register_handler(self, handler):
        if handler.__name__ in self.__handlers:
            raise Exception(
                f"Trying to register duplicate handler for name {handler.__name__}"
            )

        self.__handlers[handler.__name__.lower()] = handler()

    def __get_handler(self, handler_name):
        return self.__handlers.get(handler_name.lower(), NotFound())

    def on_message(self, message):
        handler = self.__get_handler(message.get("handler", "not_found"))
        action = message.get("action", "not_found")
        data = message.get("data", {})
        return handler.dispatch(action, data)
