from database.models import db
from database.models import Cluster

db.create_all()

cluster1 = Cluster(name='cluster1', asset='grn:/sumano', control_plane_label='cluster1',dns_subdomain='sumano.kod.ms.com')

db.session.add(cluster1)
db.session.commit()
