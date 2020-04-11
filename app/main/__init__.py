from flask import Blueprint

http = Blueprint(r"http", __name__)
ws = Blueprint(r"ws", __name__)

from . import routes, events
