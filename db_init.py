from database.models import db
from database.models import Cluster

db.create_all()

cluster1 = Cluster(name='cluster1', asset='grn:/sumano', control_plane_label='cluster1',dns_subdomain='sumano.kod.ms.com',node_id=1)
cluster2 = Cluster(name='cluster2', asset='grn:/sumano2', control_plane_label='cluster2',dns_subdomain='cluster2.kod.ms.com',node_id=1)

db.session.add(cluster1)
db.session.add(cluster2)
db.session.commit()
