import time
import json
import requests
import re
import asyncio

from ..codes import MSG_FIELD, GRID_EVENTS, NODE_EVENTS, WORKER_PROPERTIES
from ..utils.wrappers import threaded


class Worker(object):
    def __init__(self, id: str, socket):
        self._id = id
        self._socket = socket
        self._ping = 0
        self._status = WORKER_PROPERTIES.ONLINE
        self.connected_nodes = {}
        self.hosted_models = {}
        self.hosted_datasets = {}
        self.cpu_percent = 0
        self.mem_usage = 0

    @property
    def status(self):
        if not self._socket:
            return WORKER_PROPERTIES.OFFLINE
        elif self._ping < WORKER_PROPERTIES.PING_THRESHOLD:
            return WORKER_PROPERTIES.ONLINE
        else:
            return WORKER_PROPERTIES.BUSY

    @property
    def address(self):
        if self._socket:
            addr = self._socket.environ["REMOTE_ADDR"]
            return re.sub("[:f]", "", addr)

    @property
    def location(self):
        if self.address:
            url = "http://ip-api.com/json/{}".format(self.address)
            r = requests.get(url)
            result = json.loads(r.text)
            if result["status"] == "success":
                return {
                    "region": result["regionName"],
                    "country": result["country"],
                    "city": result["city"],
                }
            else:
                return {}

    def send(self, message):
        self._socket.send(message)

    # Run it in a different thread
    @threaded
    def monitor(self):
        while self._socket:
            self.__begin = time.time()
            self._socket.send(json.dumps({MSG_FIELD.TYPE: NODE_EVENTS.MONITOR}))
            time.sleep(WORKER_PROPERTIES.HEALTH_CHECK_INTERVAL)

    def update_node_infos(self, message):
        if self.__begin:
            end = time.time()
            self._ping = (end - self.__begin) * 1000
            self.connected_nodes = message[MSG_FIELD.NODES]
            self.hosted_models = message[MSG_FIELD.MODELS]
            self.hosted_datasets = message[MSG_FIELD.DATASETS]
            self.cpu_percent = message[MSG_FIELD.CPU]
            self.mem_usage = message[MSG_FIELD.MEM_USAGE]
