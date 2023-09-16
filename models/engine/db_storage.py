#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, (create_engine)

class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(sys.argv[1], sys.argv[2], 
                                              sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
