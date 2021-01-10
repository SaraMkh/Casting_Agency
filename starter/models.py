import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import datetime

DB_Name= "Casting_Agency2"
#DB_path = "postgres://{}/{}".format('sosomohhamud@localhost:5432', DB_Name)
DB_path ='postgresql://postgres:sosomohhamud@localhost:5432/Casting_Agency2'
db=SQLAlchemy()
'''
setup the db

'''
def setup_db(app,DB_path=DB_path ):
    app.config["SQLALCHEMY_DATABASE_URI"]=DB_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.app=app
    db.init_app(app)
    #db.create_all()

'''
The Models

'''
class Movie(db.Model):
    __tablename__='Movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    date = Column( db.DateTime )

    def __init__(self,title,date ):
        self.title=title
        self.date=date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'date': self.date
        }

'''

Movies with attributes title and release date
Actors with attributes name, age and gender

'''

# class Contract(db.Model):
#     __tablename__ = 'Contract'

#     id = db.Column(db.Integer, primary_key=True)
#     movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)
#     actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), nullable=False)
 
# #    def __repr__(self):
# #       return f'<Contract: {self.id}, movie_id: {self.movie_id}, actor_id: {self.actor_id}>'
#     def __init__(self,movie_id,actor_id ):

#         self.movie_id=movie_id
#         self.actor_id=actor_id

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()


#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
'''

Movies with attributes title and release date
Actors with attributes name, age and gender

'''

class Actor(db.Model):
    __tablename__='Actor'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    age = Column(Integer)
    gender = Column(String)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)


    def __init__(self,name,age,gender,movie_id ):
        self.name=name
        self.age=age
        self.gender=gender
        self.movie_id=movie_id


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'name': self.name,
        'age': self.age,
        'gender': self.gender,
        'movie_id': self.movie_id
        }