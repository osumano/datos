from database.models import db
from database.models import Cluster
from database.models import Node

db.create_all()

cluster1 = Cluster(name='cluster1', asset='appTeam1', control_plane_label='cluster1_appteam1',dns_subdomain='mydomain.testdomain.com')
node1 = Node(name='node1',machinetype='x2.large',hostname='node1.testdomain.com',cluster_id=1)
db.session.add(cluster1)
db.session.add(node1)

db.session.commit()
