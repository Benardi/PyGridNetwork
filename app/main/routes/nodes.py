from .. import http
from ..events.socket_handler import SocketHandler
from ..codes import MSG_FIELD
from flask import Response
import json

socket_handler = SocketHandler()


@http.route("/nodes", methods=["GET"])
def connected_nodes():
    response = {}
    for node_id, node in socket_handler.nodes:
        response[node_id] = {
            "address": node.address,
            "status": node.status,
            "nodes": node.connected_nodes,
            "location": node.location,
        }

    response_body = json.dumps(response)
    return Response(response_body, status=200, mimetype="application/json")


@http.route("/node/<id>")
def node_infos(id):
    worker = socket_handler.get(id)
    response = {}

    if worker:
        response["id"] = worker._id
        response["address"] = worker.address
        response["nodes"] = worker.connected_nodes
        response["datasets"] = worker.hosted_datasets
        response["models"] = worker.hosted_models
        response_body = json.dumps(response)
        return Response(response_body, status=200, mimetype="application/json")
    else:
        return Response(
            {
                MSG_FIELD.STATUS: MSG_FIELD.ERROR,
                MSG_FIELD.CONTENT: "Worker ID not found!",
            },
            status=404,
            mimetype="application/json",
        )
