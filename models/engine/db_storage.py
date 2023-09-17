#!/usr/bin/python3
""" State Module for HBNB project """
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, (create_engine)
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None
    def __init__(self):
        """Initialize the class"""
        self.__engine = create_engine('mysql+mysqldb://HBNB_MYSQL_USER:
                                      HBNB_MYSQL_PWD@localhost/HBNB_MYSQL_DB',
                                      pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ method to list all instance as a dictionary"""
        _dict = {}
        if (cls):
            instances = self.__session.query(cls.__name__).all()
            for obj in instances:
                key = '{}.{}'.format(cls.__name__, obj.id)
                _dict[key] = obj
            self.__session.close()
        else:
            class_list = [State, City, User, Place, Review, Amenity]
            for elmt in class_list:
                 instances = self.__session.query(elmt).all()
                for obj in instances:
                    key = '{}.{}'.format(elmt, obj.id)
                    _dict[key] = obj
                self.__session.close()
        return (_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
