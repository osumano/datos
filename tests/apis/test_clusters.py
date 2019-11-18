import pytest
from datos import app, apis
from flask import request, jsonify
from datos.apiv1 import blueprint, api
import datetime

m_date = 'datostest-' + datetime.datetime.now().strftime("%y-%d-%s")

app.register_blueprint(blueprint, url_prefix='')
@pytest.fixture()
def client():
    """ instantiates test_client"""
    return app.test_client()

def test_GET_clusters(client):
       """ Get test for /clusters"""
       print("'GET method test for /clusters'")
       response = client.get('/clusters/')
       assert  b'cluster1' in response.data


@app.route('/clusters/')
def test_POST_clusters():
    with app.test_client() as c:
        rv = c.post('/clusters/', json={
            'name':  m_date, 'asset': 'datostest', 'control_plane_label': 'datostest', 'dns_subdomain': 'datostest.mydomain.com'
        })
        json_data = rv.get_json()
        print("'POST method test for /clusters'")
        print(json_data['name'])
        print(json_data)

        assert (json_data['name'] == m_date )
