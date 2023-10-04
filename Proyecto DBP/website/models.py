# what "." means is that "from this package (referring from everyuthing inside init.py) get me db"
# this will be equivalent to write "from website import db"
from . import db
# custom class we can inherent that gives clases the ability to use login functions
from flask_login import UserMixin
from sqlalchemy.sql import func

# defining objets for our db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # setting up a relationship with the otherdb by using the primary key of the other db as a foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# using a one to many relationship
# each user can have multiple keys


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # setting up a relationship with the otherdb by using the primary key of the other db as a foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))