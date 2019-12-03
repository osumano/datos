from flask_restplus import Namespace, Resource, fields
from database.models import Node
from flask import request
from database.models import Cluster, Node, db
from sqlalchemy import exc

api = Namespace('nodes', description='Nodes operations')


node = api.model('nodes', {
    'name': fields.String(required=True, description='cluster name'),
    'hostname': fields.String(required=True, description='asset name for this cluster'),
    'machinetype': fields.String(required=True, description='node machinetype '),
    #'cluster_name': fields.String(required=True, description='cluster_name reference ')
    'cluster_id': fields.Integer(required=True, description='cluster reference')

})
@api.route('/')
class NodesList(Resource):
    @api.doc('List all nodes')
    @api.marshal_with(node)
    def get(self):
        '''List all nodes'''
        return Node.query.all()

    @api.doc('create node')
    @api.expect(node)
    @api.marshal_with(node, skip_none=True)
    def post(self):
      '''Create a new node'''
      req_data = request.get_json()
      required = ['name', 'hostname', 'machinetype', 'cluster_name']
      if not all(value in req_data for value in required):
          return 'Missing values', 400
      n_name = req_data['name']
      n_hostname = req_data['hostname']
      n_machinetype = req_data['machinetype']
      n_cluster_name = req_data['cluster_name']

      check_cluster = Cluster.query.filter_by(name=n_cluster_name).first()

      if  check_cluster:
          pass
      else:
          return None, 422



      check_node = Node.query.filter_by(name=n_name).first()
      if None  in (n_name, n_hostname, n_machinetype, n_cluster_name):
          return None, 422

      if check_node:
          return None, 409
      else:
          new_node = Node(name=n_name, hostname=n_hostname, machinetype=n_machinetype, cluster_id=check_cluster.id )
          db.session.add(new_node)
          db.session.commit()
          return req_data, 201
