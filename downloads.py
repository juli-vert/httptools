from turtle import ht
from flask import (Flask, json, make_response, redirect, 
                Response, send_file, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)
import time
from http_status import http_status

bprint = Blueprint('download', __name__, url_prefix='/download')

@bprint.route('/<size>', methods=['GET'])
def initbp(size):
    """Endpoint to test different HTTP status code
    Get a response with different status.
    ---
    parameters:
      - name: size
        in: path
        type: string
        required: true
    definitions:
      Size:
        type: string
    responses:
      200:
        description: A simple response
        schema:
          $ref: '#/definitions/Size'
        examples:
          size: ['small', 'medium', 'large']
    """
    files = {
      "small": "10MB.zip",
      "medium": "50MB.zip",
      "large" : "200MB.zip"
    }

    return send_file(f"./files/{files.get(size, 'small')}")