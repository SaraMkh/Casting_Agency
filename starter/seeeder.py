from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import setup_db, Movie, Actor
from sqlalchemy.ext.declarative import declarative_base
import sys


engine = create_engine('postgresql+psycopg2://sosomohhamud@localhost/Casting_Agency2')

DBSession = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)
Base.metadata.bind = engine

session = DBSession()
'''


'''
movie1 = Movie( title="Rain Man", date="1988-12-16T21:30:00.000Z")
movie2 = Movie( title="Hulk", date="2003-06-20T21:30:00.000Z")
movie3 = Movie( title="The Forest", date="2016-01-08T09:30:00.000Z")
session.add_all([movie1, movie2, movie3])
session.commit()
session.close()


'''

'''
actor1 = Actor( name="Thomas Cruise Mapother", age=58, gender="Male", movie_id=1)
actor2 = Actor( name="Valeria Golino", age=55, gender="Female", movie_id=1)
actor3 = Actor( name="Eric Banadinović ", age=53, gender="Male", movie_id=2)
actor4 = Actor( name="Natalie Dormer", age=38, gender="Female", movie_id=3)
actor5 = Actor( name="Eoin Christopher Macken", age=37, gender="Male", movie_id=3)
session.add_all([actor1, actor2, actor3, actor4, actor5])
session.commit()
session.close()