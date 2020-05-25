from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from flask import Flask, Blueprint
from flask_sockets import Sockets

ws = Blueprint(r"ws", __name__)
http = Blueprint(r"http", __name__)
DEFAULT_SECRET_KEY = "justasecretkeythatishouldputhere"
__version__ = "0.1.0"

def create_app(debug=False, secret_key=DEFAULT_SECRET_KEY):
    app = Flask(__name__)
    app.debug = debug
    app.config["SECRET_KEY"] = secret_key

    # Global socket handler
    sockets = Sockets(app)

    app.register_blueprint(http, url_prefix=r"/")
    sockets.register_blueprint(ws, url_prefix=r"/")

    return app

def raise_grid():
    app = create_app()
    server = pywsgi.WSGIServer(("", 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
    return app, server
