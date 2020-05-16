import threading
import json
import time

from .socket_handler import SocketHandler
from ..codes import MSG_FIELD

socket_handler = SocketHandler()


def update_node(message, socket):
    try:
        worker = socket_handler.get(socket)
        worker.update_node_infos(message)
    except Exception:
        pass


def register_node(message, socket):
    try:
        time.sleep(1)
        node_id = message[MSG_FIELD.NODE_ID]
        worker = socket_handler.new_connection(node_id, socket)
        t = threading.Thread(target=worker.monitor)
        t.start()
        return {"status": "success!"}
    except Exception:
        pass


def forward(message, socket):
    try:
        time.sleep(1)
        dest = message[MSG_FIELD.DESTINATION]
        worker = socket_handler.get(dest)
        if worker:
            content = message[MSG_FIELD.CONTENT]
            worker.send(json.dumps(content))
    except Exception:
        pass
