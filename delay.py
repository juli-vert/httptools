from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)
import time

bprint = Blueprint('delay', __name__, url_prefix='/delay')

@bprint.route('/<timer>', methods=['GET'])
def initbp(timer):
    """Endpoint to test delayed responses
    Add delay to a response.
    ---
    parameters:
      - name: timer
        in: path
        type: integer
        required: true
    definitions:
      Timer:
        type: integer
    responses:
      200:
        description: A simple response
        schema:
          $ref: '#/definitions/Timer'
        examples:
          rgb: ['1', '5', '10']
    """
    time.sleep(int(timer))
    return render_template("home.jinja2")