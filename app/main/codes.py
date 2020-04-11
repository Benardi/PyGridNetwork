class EVENT_ROUTES:
    JOIN = "join"
    PING = "ping"
    FORWARD = "forward"
    UPDATE_MODELS = "update-models"
    UPDATE_DATASETS = "update-dataset"
    UPDATE_NODES = "update-nodes"
    FORWARD = "forward"


class WORKER_STATUS:
    ONLINE = 1
    OFFLINE = 2
    BUSY = 3


class MSG_FIELD:
    TYPE = "type"
    MODELS = "get-models"
    DATASETS = "get-datasets"
    NODES = "get-nodes"
    FROM = "from"
    DESTINATION = "destination"
    CONTENT = "content"


class WORKER_PROPERTIES:
    HEALTH_CHECK_INTERVAL = 15
    ONLINE = "online"
    BUSY = "busy"
    OFFLINE = "offline"
