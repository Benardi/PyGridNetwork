from .socket_handler import SocketHandler

socket_handler = SocketHandler()


def update_model_infos(message, socket):
    worker = socket_handler.get(socket)
    worker._model_infos = message


def update_dataset_infos(message, socket):
    worker = socket_handler.get(socket)
    worker._dataset_infos = message


def update_connected_nodes(message, socket):
    worker.socket_handler.get(socket)
    worker._connected_nodes = message
