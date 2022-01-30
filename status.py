from turtle import ht
from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)
import time
from http_status import http_status

bprint = Blueprint('status', __name__, url_prefix='/status')

@bprint.route('/<status>', methods=['GET'])
def initbp(status):
    """Endpoint to test different HTTP status code
    Get a response with different status.
    ---
    parameters:
      - name: status
        in: path
        type: integer
        required: true
    definitions:
      Status:
        type: integer
    responses:
      200:
        description: A simple response
        schema:
          $ref: '#/definitions/Status'
        examples:
          status: ['200', '404', '503']
    """
    if int(status) in http_status.keys():
        return Response(http_status.get(int(status)), status=status)
    return Response(http_status.get(500), status=500)