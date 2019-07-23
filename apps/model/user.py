from apps.extensions import db


class User(db.Model):
    id = db.Column(db.Integer)
    user = db.Column(db.String(24))
