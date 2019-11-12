from database.models import db
from database.models import Cluster
from database.models import Node

db.create_all()

cluster1 = Cluster(name='cluster1', asset='grn:/sumano', control_plane_label='cluster1',dns_subdomain='sumano.kod.ms.com')
node1 = Node(name='node1',hostname='node1.ms.com',cluster_id=1)
db.session.add(cluster1)
db.session.add(node1)

db.session.commit()
