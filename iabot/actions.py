from flask import jsonify, request


class FlaskEndPointAction(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, *args, **kwargs):
        return jsonify(
            self.action(
                request.json
            )
        )
