from flask import Flask
import os

app = Flask(__name__)
if  os.environ['APP_ENV'] == 'dev':
   app.config.from_object('config.DevelopmentConfig')
elif os.environ['APP_ENV'] == 'devdocker':
    app.config.from_object('config.DevelopmentConfigDocker')
