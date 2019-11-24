from flask_restplus import Namespace, Resource, fields
from flask import request
from database.models import Cluster, db
from sqlalchemy import exc

api = Namespace('clusters', description='Cluster operations')


cluster = api.model('clusters', {
    'name': fields.String(required=True, description='cluster name'),
    'asset': fields.String(required=True, description='asset name for this cluster'),
    'control_plane_label': fields.String(required=True, description='control plane label - used for automation'),
    'dns_subdomain': fields.String(description='dns_subdomain field for clusters')

})
#POST & GET
@api.route('/')
class ClusterList(Resource):
    @api.doc('List all clusters')
    @api.marshal_with(cluster)
    def get(self):
        '''List all clusters'''
        return Cluster.query.all()

    @api.doc('create cluster')
    @api.expect(cluster)
    @api.marshal_with(cluster, skip_none=True)
    def post(self):
        '''Create a new cluster'''
        req_data = request.get_json()
        required = ['name', 'asset', 'control_plane_label', 'dns_subdomain']
        if not all(value in req_data for value in required):
            return 'Missing values', 400
        n_name = req_data['name']
        n_asset = req_data['asset']
        n_control_plane_label = req_data['control_plane_label']
        n_dns_subdomain = req_data['dns_subdomain']
        check_cluster = Cluster.query.filter_by(name=n_name).first()
        if None  in (n_name, n_asset, n_control_plane_label, n_dns_subdomain):
            return None, 422

        if check_cluster:
            return None, 409
        else:
            new_cluster = Cluster(name=n_name, asset=n_asset, control_plane_label=n_control_plane_label, dns_subdomain=n_dns_subdomain )
            db.session.add(new_cluster)
            db.session.commit()
            return req_data, 201

    @api.doc('update cluster ')
    @api.expect(cluster)
    @api.marshal_with(cluster, skip_none=True)
    def put(self):
        '''Update a  cluster'''
        req_data = request.get_json()
        required = ['name', 'asset', 'control_plane_label', 'dns_subdomain']
        if not all(value in req_data for value in required):
            return 'Missing values', 400
        n_name = req_data['name']
        n_asset = req_data['asset']
        n_control_plane_label = req_data['control_plane_label']
        n_dns_subdomain = req_data['dns_subdomain']
        if None  in (n_name, n_asset, n_control_plane_label, n_dns_subdomain):
            return None, 422  #user didnt provide all the fields

        check_cluster = Cluster.query.filter_by(name=n_name).first()
        if check_cluster:
            update_cluster = Cluster.query.filter_by(name=n_name).first()
            update_cluster.name = n_name
            update_cluster.asset = n_asset
            update_cluster.control_plane_label = n_control_plane_label
            update_cluster.dns_subdomain = n_dns_subdomain
            db.session.commit()
            return req_data, 200
        else:
            return None, 404




#GET by cluster name and DELETE by cluster name
@api.route('/<name>')
@api.response(404, 'Cluster not found')
@api.param('name', 'The cluster identifier')
class ClusterGet(Resource):
    '''Show a single cluster record and lets you delete them'''
    @api.doc('List a cluster by name')
    @api.marshal_with(cluster)
    def get(self, name):
        '''List a cluster by name '''
        return Cluster.query.filter_by(name=name).first_or_404()

    @api.doc('Delete cluster record')
    @api.marshal_with(cluster, skip_none=True)
    @api.response(204, 'Cluster record deleted')
    def delete(self, name):
        '''Delete a cluster by name'''
        d_cluster = Cluster.query.filter_by(name=name).first_or_404()

        try:
           db.session.delete(d_cluster)
           db.session.commit()
        except exc.IntegrityError:
           db.session().rollback()
           return None, 500
        return '', 204
