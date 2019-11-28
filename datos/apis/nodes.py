from flask_restplus import Namespace, Resource, fields
from database.models import Node

api = Namespace('nodes', description='Nodes operations')


node = api.model('nodes', {
    'name': fields.String(required=True, description='cluster name'),
    'hostname': fields.String(required=True, description='asset name for this cluster'),
    'cluster_id': fields.Integer(required=True, description='cluster reference')

})
@api.route('/')
class NodesList(Resource):
    @api.doc('List all nodes')
    @api.marshal_with(node)
    def get(self):
        '''List all nodes'''
        return Node.query.all()
