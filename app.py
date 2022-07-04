from flask import Flask
from datetime import timedelta
from flasgger import Swagger # https://github.com/flasgger/flasgger#installation
import delay, status, redirect, req_inspect, kube, method

app = Flask(__name__)
swagger = Swagger(app)
app.config.from_object(__name__)

# Blueprints
app.register_blueprint(delay.bprint)
app.register_blueprint(status.bprint)
app.register_blueprint(redirect.bprint)
app.register_blueprint(req_inspect.bprint)
app.register_blueprint(kube.bprint)
app.register_blueprint(method.bprint)
