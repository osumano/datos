from flask_restplus import Namespace, Resource, fields
from database.models import Cluster

api = Namespace('clusters', description='Cluster operations')

@api.route('/')
class ClustersList(Resource):
    @api.doc('List all clusters')
    def get(self):
        '''List all clusters'''
        return Cluster.query.all()
        #return 'success'
