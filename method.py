from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)
import requests
bprint = Blueprint('method', __name__, url_prefix='/method')

@bprint.route('/post', methods=['POST'])
def post():
    """A basic POST endpoint
    Get the request body.
    ---
    responses:
      200:
        description: body
    """
    body = request.json
    return body
