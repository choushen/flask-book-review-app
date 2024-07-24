from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500),unique=True, index=True, nullable=False)
    password = db.Column(db.String(500))
    email = db.Column(db.String(500), nullable=False)
    start_date = db.Column(db.DateTime)
    books = db.relationship('Collection', backref='collection', lazy='dynamic')

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(500), unique=True, index=True, nullable=False)
    description = db.Column(db.String(500))
    author = db.Column(db.String(500))
    read = db.Column(db.Boolean(False))
    review = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
