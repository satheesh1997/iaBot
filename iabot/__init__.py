from iabot.handlers import NotFoundHandler


class CreateBot(object):
    __handlers = {}

    def __init__(self, handlers):
        if not type(handlers) == list:
            raise Exception("Handlers must be of type list")

        for handler in handlers:
            self.__register_handler(handler)

    def __register_handler(self, handler):
        if not hasattr(handler, "handle"):
            raise Exception(f"Handler {handler.__name__} has no attribute handle")
        if not type(handler.handle) == str:
            raise AttributeError(
                f"Handler {handler.__name__} attr handle must be of type str"
            )
        if handler.handle in self.__handlers:
            raise Exception(
                f"Trying to register duplicate handler for name {handler.__name__}"
            )

        handle_name = handler.handle.lower()
        self.__handlers[handle_name] = handler()

    def __get_handler(self, handler_name):
        return self.__handlers.get(handler_name.lower(), NotFoundHandler())

    def on_message(self, message):
        handler = self.__get_handler(message.get("handler", "not_found"))
        action = message.get("action", "not_found")
        data = message.get("data", {})
        return handler.dispatch(action, data)
