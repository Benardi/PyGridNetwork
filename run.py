#!/bin/env python

from app import create_app


from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


if __name__ == "__main__":
    app = create_app()
    server = pywsgi.WSGIServer(("", 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
else:
    app = create_app()
