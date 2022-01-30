from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)
bprint = Blueprint('inspect', __name__, url_prefix='/inspect')

@bprint.route('/headers', methods=['GET'])
def initbp():
    """Endpoint to show request headers
    Get the request headers.
    ---
    responses:
      200:
        description: headers
    """
    res = {}
    for header in request.headers:
      res[header[0]] = header[1:]
    return jsonify(res)