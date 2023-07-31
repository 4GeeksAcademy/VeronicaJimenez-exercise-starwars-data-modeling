import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    favorites = relationship ('Favorites', backref = 'favorites', lazy=True)  

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column (Integer, primary_key=True)
    planets = relationship ('Planets', backref='favorites', lazy=True)
    Characters = relationship ('Characters', backref='favorites', lazy=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
      

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height =  Column(Integer)
    mass = Column(Integer)
    planets_id = Column (Integer, ForeignKey('planets.id'), nullable=False) 
    favorites_id = Column (Integer, ForeignKey('favorites.id'), nullable=False)
    


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))    
    gravity = Column(Integer)
    name = Column(String(250), nullable=False)
    orbital_period = Column(Integer)
    population = Column(Integer)
    characters = relationship('Characters',backref='planets', lazy=True)
    favorites_id = Column (Integer, ForeignKey('favorites.id'), nullable=False)
   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')