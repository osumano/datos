from flask import Blueprint
from flask_restplus import Api

api = Api(blueprint)

from .apis.clusters import api as clusters

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_namespace(clusters)
