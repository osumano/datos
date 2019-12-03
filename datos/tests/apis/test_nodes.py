import pytest
from datos import app, apis
from flask import request, jsonify
from datos.apiv1 import blueprint, api
import datetime

m_date = 'node-datostest-' + datetime.datetime.now().strftime("%y-%d-%s")

#app.register_blueprint(blueprint, url_prefix='')
@pytest.fixture()
def client():
    """ instantiates test_client"""
    return app.test_client()

def test_GET_nodes(client):
       """ Get test for /nodes"""
       print("\n'GET method test for /nodes'")
       response = client.get('/nodes/')
       assert  b'node1' in response.data


@app.route('/nodes/')
def test_POST_nodes():
    with app.test_client() as c:
        rv = c.post('/nodes/', json={
            'name':  m_date, 'hostname': 'node-datostest', 'machinetype': 'x2.large', 'cluster_name': 'cluster1'
        })
        json_data = rv.get_json()
        print("\n'POST method test for /nodes'")
        assert (json_data['name'] == m_date )
