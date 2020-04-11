from .socket_handler import SocketHandler
import threading

socket_handler = SocketHandler()


def health_check(message, socket):
    worker = socket_handler.get(socket)
    worker.update_ping_rate()


def register_node(message, socket):
    node_id = message["id"]
    worker = socket_handler.new_connection(node_id, socket)
    t = threading.Thread(target=worker.check_health)
    t.start()
    return {"status": "success!"}


def forward(message, socket):
    dest = message["destination"]
    worker = socket_handler.get(dest)
    if worker:
        worker.send(message["content"])
