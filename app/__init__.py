from flask import Flask
from flask_sockets import Sockets

DEFAULT_SECRET_KEY = "justasecretkeythatishouldputhere"


def create_app(debug=False, secret_key=DEFAULT_SECRET_KEY):
    app = Flask(__name__)
    app.debug = debug
    app.config["SECRET_KEY"] = secret_key

    from .main import http, ws

    # Global socket handler
    sockets = Sockets(app)

    app.register_blueprint(http, url_prefix=r"/")
    sockets.register_blueprint(ws, url_prefix=r"/")

    return app
