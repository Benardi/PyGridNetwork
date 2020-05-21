from .socket_handler import SocketHandler
from ..codes import MSG_FIELD
import threading
import json
import time

socket_handler = SocketHandler()


def update_node(message, socket):
    worker = socket_handler.get(socket)
    worker.update_node_infos(message)


def register_node(message, socket):
    time.sleep(1)
    node_id = message[MSG_FIELD.NODE_ID]
    worker = socket_handler.new_connection(node_id, socket)
    t = threading.Thread(target=worker.monitor)
    t.start()
    return {"status": "success!"}


def forward(message, socket):
    time.sleep(1)
    dest = message[MSG_FIELD.DESTINATION]
    worker = socket_handler.get(dest)
    if worker:
        content = message[MSG_FIELD.CONTENT]
        worker.send(json.dumps(content))
