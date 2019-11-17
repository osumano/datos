from flask_sqlalchemy import SQLAlchemy
from datos import app

db = SQLAlchemy(app)


class Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    asset = db.Column(db.String(256), nullable=False)
    control_plane_label = db.Column(db.String(256), nullable=False)
    dns_subdomain = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "<Cluster '{}'>".format(self.name)



class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hostname = db.Column(db.String(250), nullable=False)

    cluster_id = db.Column(db.Integer, db.ForeignKey('cluster.id'),
       nullable=False)

    cluster = db.relationship('Cluster',
        backref=db.backref('nodes', lazy=True))


    def __repr__(self):
        return "<Node '{}'>".format(self.name)
