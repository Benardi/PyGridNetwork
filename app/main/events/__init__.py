from .. import ws
from ..codes import MSG_FIELD, EVENT_ROUTES

from .socket_handler import SocketHandler
from .network import register_node, health_check, forward
from .node_properties import *
import json

socket_handler = SocketHandler()

routes = {
    EVENT_ROUTES.JOIN: register_node,
    EVENT_ROUTES.PING: health_check,
    EVENT_ROUTES.FORWARD: forward,
    EVENT_ROUTES.UPDATE_MODELS: update_model_infos,
    EVENT_ROUTES.UPDATE_DATASETS: update_dataset_infos,
    EVENT_ROUTES.UPDATE_NODES: update_connected_nodes,
}


def route_request(message, socket):
    global routes

    message = json.loads(message)

    if message and message.get(MSG_FIELD.TYPE, None) in routes.keys():
        return routes[message[MSG_FIELD.TYPE]](message, socket)
    else:
        return {"status": "error", "message": "Invalid request format!"}


@ws.route("/")
def socket_api(socket):
    while not socket.closed:
        message = socket.receive()
        if not message:
            continue
        else:
            response = route_request(message, socket)
            if response:
                socket.send(json.dumps(response))

    worker_id = socket_handler.remove(socket)
