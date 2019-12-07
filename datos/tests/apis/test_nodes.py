import pytest
from datos import app, apis
from flask import request, jsonify
from datos.apiv1 import blueprint, api
import datetime

m_date = 'node-datostest-' + datetime.datetime.now().strftime("%y-%d-%s")

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

def test_GET_node_byname(client):
       """ Get test for /nodes/<name>"""
       print("\nGET method test for /nodes/" + m_date)
       response = client.get('/nodes/' + m_date )
       assert m_date.encode()  in response.data


def test_PUT_nodes():
    with app.test_client() as c:
        rv = c.put('/nodes/', json={
            'name':  m_date, 'hostname': 'node-datostest-update', 'machinetype': 'x2.large', 'cluster_name': 'cluster1'
        })
        json_data = rv.get_json()
        print("\n'PUT method test for /nodes/'")
        assert (json_data['name'] == m_date )

def test_DELETE_node_byname(client):
        """ DELETE test for /nodes/<name>"""
        print("\nDELETE method test for /nodes/" + m_date)
        response = client.delete('/nodes/' + m_date )
        assert response.status_code == 204
