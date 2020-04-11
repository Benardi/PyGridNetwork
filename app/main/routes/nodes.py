from .. import http
from ..events.socket_handler import SocketHandler

from flask import Response
import json

socket_handler = SocketHandler()


@http.route("/nodes", methods=["GET"])
def connected_nodes():
    response = {}
    for node in socket_handler.nodes:
        response[node._id] = {
            "address": node.address,
            "status": node.status,
            "nodes": node.connected_nodes,
        }

    response_body = json.dumps(response)
    return Response(response_body, status=200, mimetype="application/json")


@http.route("/node/<id>")
def node_infos(node_id):
    worker = socket_handler.get(node_id)
    response = {}
    if worker:
        response["id"] = worker._id
        response["address"] = worker.address
        response["nodes"] = worker.connected_nodes
        response["datasets"] = worker.datasets
        response["models"] = worker.models
        response_body = json.dumps(response)
        return Response(response_body, status=200, mimetype="application/json")
    else:
        return Response("", status=500, mimetype="application/json")
