from app import db
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
'''

Movies with attributes title and release date
Actors with attributes name, age and gender

''''

DB_Name= "Casting_Agency"
database_path = "postgres://{}/{}".format('localhost:5432', DB_Name)
db.SQLAlchemy()
class Movie(db.Model):
    __tablename__='Movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    date = Column(DataTime())