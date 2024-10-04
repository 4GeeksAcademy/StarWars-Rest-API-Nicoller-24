"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Planetas, PersonajesFavoritos, PlanetasFavoritos

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    all_user = list(User.query.all())
    results = list(map(lambda user: user.serialize(), all_user)) 
   
    return jsonify(results), 200

@app.route('/people', methods=['GET'])
def get_personajes():
    all_characters = list(Personajes.query.all()) 
    results = list(map(lambda character: character.serialize(), all_characters)) 

    return jsonify(results), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_personaje(people_id):
    personaje = Personajes.query.filter_by(id=people_id).first()
    
    if personaje is None:
        return jsonify({"error": "Personaje no encontrado"}), 404
    
    return jsonify(personaje.serialize()), 200


@app.route('/planets', methods=['GET'])
def get_planetas():
    all_planets = list(Planetas.query.all()) 
    results = list(map(lambda planet: planet.serialize(), all_planets)) 

    return jsonify(results), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planeta(planet_id):
    planeta = Planetas.query.filter_by(id=planet_id).first()
    
    if planeta is None:
        return jsonify({"error": "Planeta no encontrado"}), 404
    
    return jsonify(planeta.serialize()), 200

@app.route('/users/favorites', methods=['GET'])
def get_favorites():
    all_planets = list(Planetas.query.all()) 
    results = list(map(lambda planet: planet.serialize(), all_planets)) 

    return jsonify(results), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
