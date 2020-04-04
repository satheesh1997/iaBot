from iabot.constants import ACTION_ERROR


class BaseHandler(object):
    def clean_response(self, resp):
        return resp

    def dispath(self, action, data):
        if type(data) is not dict:
            resp = {
                "status": ACTION_ERROR,
                "response": {"message": "Data must be of type for smooth dispatch"},
            }
        else:
            try:
                dispatch_action = getattr(self, action)
            except Exception as e:
                print(e)
                dispatch_action = getattr(self, "not_found")

            resp = dispatch_action(data)

        return self.clean_response(resp)

    def not_found(self, *args, **kwargs):
        return {
            "status": ACTION_ERROR,
            "response": {"message": "Action not defined in the handler"},
        }
