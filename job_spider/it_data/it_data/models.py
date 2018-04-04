#!/usr/bin/env python

#coding:utf8

#orm -> sqlalchemy

import sqlalchemy
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Itdata(Base):
    __tablename__ = 'Itdata'
    Id = Column(Integer, primary_key=True,unique=True, nullable=False, autoincrement=True)
    fromsite = Column(String(128))
    positionType = Column(String(128))
    positionName = Column(String(128))
    salary = Column(String(128))
    education = Column(String(128))
    city = Column(String(128))
    workYear = Column(String(128))
    jobDes = Column(LONGTEXT)
    company = Column(String(128))
    companySize = Column(String(128))
    financeStage = Column(String(128))
    industryField = Column(String(128))
    #--------------------------#
    rate = Column(String(128))
    number = Column(String(128))

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/itdata',echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
# session = Session()
