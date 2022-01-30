from app import app
from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)

@app.route('/', methods=['GET'])
def defaultSite():
    return render_template("home.jinja2")