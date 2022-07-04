import socket, time
import kubernetes as k8s
from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)

bprint = Blueprint('kubernetes', __name__, url_prefix='/k8s')

@bprint.route('/cluster', methods=['GET'])
def cluster():
    """Endpoint to get information about the K8s cluster
    ---
    responses:
      200:
        description: Kubernetes cluster info
    """
    res = {}
    try:
      k8s.config.load_incluster_config()
      cli = k8s.client.CustomObjectsApi()
      clusters = cli.list_cluster_custom_object(group="cluster.x-k8s.io", version="v1alpha3", plural="clusters")
      for cluster in clusters.get("items"):
        name = cluster.get("metadata").get("name")
        res.update({"cluster": name, "pod": socket.gethostname()})
      return res
    except Exception as exc:
      print(exc)
      return {}
