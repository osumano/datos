from sqlalchemy import *

engine = create_engine('postgresql://localhost/datos')


metadata = MetaData()


clusters = Table('clusters', metadata,
   Column('cluster_id', Integer, primary_key=True),
   Column('cluster_name', String(256), nullable=False),
   Column('asset', String(128), nullable=False),
   Column('environments', Integer, ForeignKey("environments.environment_id")),
   Column('oidc_endpoints', Integer, ForeignKey("oidc_endpoints.oidc_endpoint_id")),
   Column('control_plane_label', String(64), nullable=False),
   Column('dns_subdomain', String(256), nullable=False)
)

environments = Table('environments', metadata,
   Column('environment_id', Integer, primary_key=True),
   Column('environment_name', String(256), nullable=False)
)

oidc_endpoints = Table('oidc_endpoints', metadata,
   Column('oidc_endpoint_id', Integer, primary_key=True),
   Column('oidc_endpoint_name', String(256), nullable=False)
)

nodes = Table('nodes', metadata,
   Column('node_id', Integer, primary_key=True),
   Column('node_name', String(250), nullable=False),
   Column('hostname', String(250), nullable=False),
   Column('ip1', String(250)),
   Column('ip2', String(250))
)

clusters_nodes_ref = Table('clusters_nodes_ref', metadata,
   Column('clusters_nodes_ref_id', Integer, primary_key=True),
   Column('clusters', Integer, ForeignKey("clusters.cluster_id")),
   Column('nodes', Integer, ForeignKey("nodes.node_id"))
)

pod_ip_pools = Table('pod_ip_pools', metadata,
   Column('pod_ip_pool_id', Integer, primary_key=True),
   Column('pod_ip_pool', String(24), nullable=False)
)

clusters_pod_ip_pools_ref = Table('clusters_pod_ip_pools_ref', metadata,
   Column('clusters_pod_ip_pools_ref_id', Integer, primary_key=True),
   Column('clusters', Integer, ForeignKey("clusters.cluster_id")),
   Column('pod_ip_pools', Integer, ForeignKey("pod_ip_pools.pod_ip_pool_id"))
)

svc_ip_pools = Table('svc_ip_pools', metadata,
   Column('svc_ip_pool_id', Integer, primary_key=True),
   Column('svc_ip_pool', String(24), nullable=False)
)

clusters_svc_ip_pools_ref = Table('clusters_svc_ip_pools_ref', metadata,
   Column('clusters_svc_ip_pools_ref_id', Integer, primary_key=True),
   Column('clusters', Integer, ForeignKey("clusters.cluster_id")),
   Column('svc_ip_pools', Integer, ForeignKey("svc_ip_pools.svc_ip_pool_id"))
)

esx_clusters = Table('esx_clusters', metadata,
   Column('esx_cluster_id', Integer, primary_key=True),
   Column('esx_cluster_name', String(250), nullable=False),
   Column('esx_vcenter_url', String(250))
)

clusters_esx_clusters_ref = Table('clusters_esx_clusters_ref', metadata,
   Column('clusters_esx_clusters_ref_id', Integer, primary_key=True),
   Column('clusters', Integer, ForeignKey("clusters.cluster_id")),
   Column('esx_clusters', Integer, ForeignKey("esx_clusters.esx_cluster_id"))
)

metadata.create_all(engine)
