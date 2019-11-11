from flask import Flask
from apiv1 import blueprint as apiv1

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.register_blueprint(apiv1)
