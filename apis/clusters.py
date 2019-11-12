from flask_restplus import Namespace, Resource, fields
from database.models import Cluster

api = Namespace('clusters', description='Cluster operations')


cluster = api.model('clusters', {
    'name': fields.String(required=True, description='cluster name'),
    'asset': fields.String(required=True, description='asset name for this cluster'),
    'control_plane_label': fields.String(required=True, description='control plane label - used for automation'),
    'dns_subdomain': fields.String(description='dns_subdomain field for clusters')

})
@api.route('/')
class ClustersList(Resource):
    @api.doc('List all clusters')
    @api.marshal_with(cluster)
    def get(self):
        '''List all clusters'''
        return Cluster.query.all()
