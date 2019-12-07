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

    @api.doc('update node ')
    @api.expect(node)
    @api.marshal_with(node, skip_none=True)
    def put(self):
        '''Update a  node'''
        req_data = request.get_json()
        required = ['name', 'hostname', 'machinetype', 'cluster_name']
        if not all(value in req_data for value in required):
            return 'Missing values', 400
        n_name = req_data['name']
        n_hostname = req_data['hostname']
        n_machinetype = req_data['machinetype']
        n_cluster_name = req_data['cluster_name']
        if None  in (n_name, n_hostname, n_machinetype, n_cluster_name):
            return None, 422  #user didnt provide all the fields

        check_node = Node.query.filter_by(name=n_name).first()
        if check_node:
            update_node = Node.query.filter_by(name=n_name).first()
            update_node.name = n_name
            update_node.hostname = n_hostname
            update_node.machinetype = n_machinetype
            update_node.cluster_name = n_cluster_name
            db.session.commit()
            return req_data, 200
        else:
            return None, 404



#GET by Node name and DELETE by node name
@api.route('/<name>')
@api.response(404, 'Node not found')
@api.param('name', 'The node identifier')
class NodeGet(Resource):
    '''Show a single node record and lets you delete them'''
    @api.doc('List a node by name')
    @api.marshal_with(node)
    def get(self, name):
        '''List a node by name '''
        return Node.query.filter_by(name=name).first_or_404()

    @api.doc('Delete node record')
    @api.marshal_with(node, skip_none=True)
    @api.response(204, 'Node record deleted')
    def delete(self, name):
        '''Delete a node by name'''
        d_node = Node.query.filter_by(name=name).first_or_404()

        try:
           db.session.delete(d_node)
           db.session.commit()
        except exc.IntegrityError:
           db.session().rollback()
           return None, 500
        return '', 204
