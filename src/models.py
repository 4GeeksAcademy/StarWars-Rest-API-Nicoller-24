from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Tabla intermedia PersonajesFavoritos
class PersonajesFavoritos(db.Model):
    __tablename__ = 'personajes_favoritos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    personaje_id = db.Column(db.Integer, ForeignKey('personajes.id'))
    
    user = relationship("User", back_populates="personajes_favoritos")
    personaje = relationship("Personajes", back_populates="favorited_by")

    def __repr__(self):
        return '<PersonajesFav %r>' % self.user_id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
            "user_name": self.user.user_name,
            "personaje_name": self.personaje.name
        }

# Tabla intermedia PlanetasFavoritos
class PlanetasFavoritos(db.Model):
    __tablename__ = 'planetas_favoritos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    planeta_id = db.Column(db.Integer, ForeignKey('planetas.id'))
    
    user = relationship("User", back_populates="planetas_favoritos")
    planeta = relationship("Planetas", back_populates="favorited_by")

    def __repr__(self):
        return '<PlanetasFav %r>' % self.user_id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "planeta_id": self.planeta_id,
            "user_name": self.user.user_name,
            "planeta_name": self.planeta.name
        }

# Clase Personajes
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)

    favorited_by = relationship('PersonajesFavoritos', back_populates='personaje')

    def __repr__(self):
        return '<Personajes %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }

# Clase Planetas
class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    favorited_by = relationship('PlanetasFavoritos', back_populates='planeta')

    def __repr__(self):
        return '<Planetas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
        }

# Clase User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    personajes_favoritos = relationship('PersonajesFavoritos', back_populates='user')
    planetas_favoritos = relationship('PlanetasFavoritos', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "email": self.email,
        }
