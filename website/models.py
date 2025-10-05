from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class Tabella(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cognome = db.Column(db.String(100), unique=True, nullable=False)
    checked = db.Column(db.Boolean, default=False, nullable=False)
    punti = db.Column(db.Integer, default=0, nullable=False)
    probabilita = db.Column(db.Float, default=0.0, nullable=False)
    stato = db.Column(db.String(10), default='----------', nullable=False)  # 10 chars: - empty, G green, R red
