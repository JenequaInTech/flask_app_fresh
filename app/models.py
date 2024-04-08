from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username' : self.username
        }
    
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)

    def __init__(self, name, img, species):
        self.name = name
        self.img = img
        self.species = species

    def save_poke(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'img' : self.img,
            'species' : self.species
        }

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pok1 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok2 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok3 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok4 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok5 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))

    def __init__(self, user_id, pok1=None, pok2=None, pok3=None, pok4=None, pok5=None):
        self.user_id = user_id
        self.pok1 = pok1
        self.pok2 = pok2
        self.pok3 = pok3
        self.pok4 = pok4
        self.pok5 = pok5

    def save_team(self):
        db.session.add(self)
        db.session.commit()