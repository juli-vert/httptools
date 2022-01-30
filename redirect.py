from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)
import time

bprint = Blueprint('redirect', __name__, url_prefix='/redirect')

@bprint.route('/', methods=['GET'])
def initbp():
    """Endpoint to test redirections
    Get a response from a redirection.
    ---
    responses:
      307:
        description: A simple response
    """
    return redirect(url_for('redirect.redirected'), code=308)
    

@bprint.route('/redirected', methods=['GET'])
def redirected():
    return render_template("home.jinja2")
