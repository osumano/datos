from flask_restplus import Namespace, Resource, fields

api = Namespace('clusters', description='Cluster operations')



@api.route('/')
class ClusterList(Resource):
    @api.doc('List all clusters')
    def get(self):
        '''List all clusters'''
        return 'hello clusters'
