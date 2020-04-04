from iabot.constants import ACTION_ERROR, ACTION_OK


class BaseHandler(object):
    def clean_response(self, resp):
        return resp

    def dispatch(self, action, data):
        if type(data) is not dict:
            resp = {
                "status": ACTION_ERROR,
                "response": {"message": "Data must be of type for smooth dispatch"},
            }
        else:
            if hasattr(self, action):
                dispatch_action = getattr(self, action)
            else:
                dispatch_action = getattr(self, "not_found")

            resp = dispatch_action(data)

        return self.clean_response(resp)

    def not_found(self, *args, **kwargs):
        return {
            "status": ACTION_ERROR,
            "response": {"message": "Action not defined in the handler"},
        }


class NotFoundHandler(BaseHandler):

    handle = "notfound"

    def dispatch(self, *args, **kwargs):
        return "Handler not registered in the bot"


class SystemInformationHandler(BaseHandler):

    handle = "system"

    def time(self, *args, **kwargs):
        import time

        return {
            "status": ACTION_OK,
            "response": {"message": time.strftime("%l:%M%p %Z")},
        }

    def date(self, *args, **kwargs):
        import time

        return {
            "status": ACTION_OK,
            "response": {"message": time.strftime("%b %d, %Y")},
        }
