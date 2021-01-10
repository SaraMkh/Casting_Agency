import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from models import setup_db, Movie, Contract, Actor
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  #CORS(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
          response.headers.add(
              'Access-Control-Allow-Headers',
              'Content-Type,Authorization,true')
          response.headers.add(
              'Access-Control-Allow-Methods',
              'GET,PATCH,POST,DELETE,OPTIONS')
          return response
  @app.route('/')
  def main_Page():
    return jsonify({'message':' Welcome to The Casting Agency company '})
  
   
'''
Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

'''
  @app.route('/movies', methods=['GET'])
  def get_movies():
          try:
              # get all available movies
              movies = Category.query.all()
              movies_Type = {}
              # create array to build the movies_type list
              for movie in movies:
                  movies_Type[movie.id] = movie.type
              return jsonify({
                'success': True,
                'movies': movies_Type
              }), 200
          except:
              abort(500)
  @app.route('/actors', methods=['GET'])
  def get_actors():
        try:
            # get all available actors
            actors = Category.query.all()
            actors_Type = {}
            # create array to build the actors_type list
            for actor in actors:
                actors_Type[actor.id] = actor.type
            return jsonify({
              'success': True,
              'actors': actors_Type
            }), 200
        except:
            abort(500)


  return app
 
APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)