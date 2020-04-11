from .. import http
from ..events import SocketHandler

from flask import Response
import json

socket_handler = SocketHandler()


@http.route("/models", methods=["GET"])
def get_models():
    response = {}

    for node in socket_handler.nodes:
        response[node._id] = node.models

    response_body = json.dumps(response)

    return Response(response_body, status_code=200, mimetype="application/json")
