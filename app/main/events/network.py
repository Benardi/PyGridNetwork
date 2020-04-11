from .socket_handler import SocketHandler
from ..codes import MSG_FIELD
import threading
import json

socket_handler = SocketHandler()


def health_check(message, socket):
    worker = socket_handler.get(socket)
    worker.update_ping_rate()


def register_node(message, socket):
    node_id = message[MSG_FIELD.NODE_ID]
    worker = socket_handler.new_connection(node_id, socket)
    t = threading.Thread(target=worker.check_health)
    t.start()
    return {"status": "success!"}


def forward(message, socket):
    dest = message[MSG_FIELD.DESTINATION]
    worker = socket_handler.get(dest)
    if worker:
        content = message[MSG_FIELD.CONTENT]
        worker.send(json.dumps(content))
