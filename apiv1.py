from flask import Blueprint
from flask_restplus import Api
from apis.clusters import api as clusters
from apis.nodes import api as nodes

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_namespace(clusters)
api.add_namespace(nodes)
