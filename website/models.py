from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


"""
class Tabella(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)
    cognome = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)
    checked = db.Column(db.Boolean, db.ForeignKey('user.id'), default=False, nullable=False)
    emoji = db.Column(db.String(32), db.ForeignKey('user.id'))
    punti = db.Column(db.Integer, db.ForeignKey('user.id'), default=0, nullable=False)
    probabilita = db.Column(db.Float, db.ForeignKey('user.id'), default=0.0, nullable=False)
"""
