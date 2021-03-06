import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth
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
  '''
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
          try:
              # get all available movies
              movies = Movie.query.all()
              return jsonify({
                'success': True,
                'movies': [moviei.format() for moviei in movies] 
              }), 200
          except:
              abort(500)

  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
        try:
            # get all available actors
            actors = Actor.query.all()
            return jsonify({
              'success': True,
              'actors': [actori.format() for actori in actors]
            }), 200
        except:
            abort(500)
  '''
  Endpoints:
  POST /actors and /movies and

  '''

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def create_movie(payload):
          body = request.get_json()
          if body is None:
              abort(401)
          new_title = body.get('title', None)
          new_date = body.get('date', None)
          try:
              new_movie = Movie(title=new_title, date=new_date)
              new_movie.insert()
              return jsonify({
                  'success': True,
                  "movies": [new_movie.format()]
              }), 200
          except Exception as error:
              raise error
  
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actor(payload):
          body = request.get_json()
          if body is None:
              abort(401)
          new_name = body.get('name', None)
          new_age = body.get('age', None)
          new_gender = body.get('gender', None)
          new_movie_id = body.get('movie_id', None)
          try:
              new_actor = Actor(name=new_name, age=new_age,gender=new_gender, movie_id=new_movie_id)
              new_actor.insert()
              return jsonify({
                  'success': True,
                  "actors": [new_actor.format()]
              }), 200
          except Exception as error:
              raise error
  '''
  Endpoints:
  PATCH /actors/ and /movies/
  '''
  @app.route('/movies/<id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie_details( payload,id):

          try:
              find_movie = Movie.query.filter(Movie.id == id).first()
              print(str(find_movie))
              if find_movie is None:
                  abort(404)
              else:
                  body = request.get_json()
                  new_title = body.get('title', None)
                  new_date = body.get('date', None)
                  find_movie.title = new_title
                  find_movie.date = new_date
                  find_movie.update()
                  return jsonify({
                      'success': True,
                      "movies": [find_movie.format()]
                      }), 200
          except Exception as error:
              raise error

  @app.route('/actors/<id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor_details( payload,id):

          try:
              find_actor = Actor.query.filter(Actor.id == id).first()
              print(str(find_actor))
              if find_actor is None:
                  abort(404)
              else:

                  body = request.get_json()
                  new_name = body.get('name', None)
                  new_age = body.get('age', None)
                  new_gender = body.get('gender', None)
                  new_movie_id = body.get('movie_id', None)
                  find_actor.name = new_name
                  find_actor.age = new_age
                  find_actor.gender = new_gender
                  find_actor.movie_id = new_movie_id
                  find_actor.update()
                  return jsonify({
                      'success': True,
                      "actors": [find_actor.format()]
                      }), 200
          except Exception as error:
              raise error

  '''
  Endpoints:
  DELETE /actors/ and /movies/
  '''

  @app.route('/movies/<id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(payload,id):
          try:
              find_movie = Movie.query.filter(Movie.id == id).first()
              if find_movie is None:
                  abort(404)
              else:
                  find_movie.delete()
                  return jsonify({
                      'success': True,
                      "movies": find_movie.id
                      }), 200
          except Exception as error:
              raise error

  @app.route('/actors/<id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(  payload,id):
          try:
              find_actor = Actor.query.filter(Actor.id == id).first()
              if find_actor is None:
                  abort(404)
              else:
                  find_actor.delete()
                  return jsonify({
                      'success': True,
                      "actors": find_actor.id
                      }), 200
          except Exception as error:
              raise error


  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False,
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  '''
  @TODO implement error handlers using the @app.errorhandler(error) decorator
      each error handler should return (with approprate messages):
              jsonify({
                      "success": False,
                      "error": 404,
                      "message": "resource not found"
                      }), 404

  '''

  '''
  @TODO implement error handler for 404
      error handler should conform to general task above
  '''


  @app.errorhandler(404)
  def resource_not_found(error):
      return jsonify({
                      "success": False,
                      "error": 404,
                      "message": "resource not found"
                      }), 404

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
                      "success": False,
                      "error": 400,
                      "message": "Bad Request"
                      }), 400


  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
                      "success": False,
                      "error": 405,
                      "message": "Method Not Allowed"
                      }), 405


  @app.errorhandler(500)
  def Internal_Server_Error(error):
      return jsonify({
                      "success": False,
                      "error": 500,
                      "message": 'Internal Server Error'
                      }), 500


  '''
  @TODO implement error handler for AuthError
      error handler should conform to general task above
  '''
  @app.errorhandler(AuthError)
  def auth_error(err):
      response = jsonify(err.error)
      response.status_code = err.status_code
      return response


  return app
 
APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)