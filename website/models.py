from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    color_facile_correct = db.Column(db.String(7), default='#a7f3bf')
    color_facile_wrong = db.Column(db.String(7), default='#ffb6c1')
    color_normale_correct = db.Column(db.String(7), default='#bfff00')
    color_normale_wrong = db.Column(db.String(7), default='#e53935')
    color_difficile_correct = db.Column(db.String(7), default='#43ea7f')
    color_difficile_wrong = db.Column(db.String(7), default='#800020')


class Tabella(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cognome = db.Column(db.String(100), unique=True, nullable=False)
    checked = db.Column(db.Boolean, default=False, nullable=False)
    punti = db.Column(db.Integer, default=0, nullable=False)
    probabilita = db.Column(db.Float, default=0.0, nullable=False)
    stato = db.Column(db.String(20), default='-'*20, nullable=False)  # 20 chars: -- empty, Gf green facile, etc.



class Storico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cognome = db.Column(db.String(100), nullable=False)
    difficolta = db.Column(db.String(20), nullable=False)
    risultato = db.Column(db.String(10), nullable=False)
    data = db.Column(db.DateTime, default=func.now())
