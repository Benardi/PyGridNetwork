import time
import json

from ..codes import MSG_FIELD, EVENT_ROUTES, WORKER_PROPERTIES


class Worker(object):
    def __init__(self, id: str, socket):
        self._id = id
        self._socket = socket
        self._ping = 0
        self._status = WORKER_PROPERTIES.ONLINE
        self._model_infos = {}
        self.dataset_infos = {}
        self.connected_nodes = {}

    @property
    def status(self):
        if not self._socket:
            return WORKER_PROPERTIES.OFFLINE
        elif self._ping < 100:
            return WORKER_PROPERTIES.ONLINE
        else:
            return WORKER_PROPERTIES.BUSY

    @property
    def models(self):
        payload = {MSG_FIELD.TYPE: MSG_FIELD.MODELS}
        self._socket.send(json.dumps(payload))

        return self._model_infos

    @property
    def datasets(self):
        payload = {MSG_FIELD.TYPE: MSG_FIELD.DATASETS}
        self._socket.send(json.dumps(payload))

        return self._dataset_infos

    @property
    def connected_nodes(self):
        payload = {MSG_FIELD.TYPE: MSG_FIELD.NODES}
        self._socket.send(json.dumps(payload))

        return self._connected_nodes

    def check_health(self):
        while not self._socket.closed:
            self.__begin = time.time()
            self._socket.send(json.dumps({MSG_FIELD.TYPE: EVENT_ROUTES.PING}))
            time.sleep(WORKER_PROPERTIES.HEALTH_CHECK_INTERVAL)

    def send(self, message):
        self._socket.send(message)

    def update_ping_rate(self):
        if self.__begin:
            end = time.time()
            self._ping = end - self.__begin * 1000
