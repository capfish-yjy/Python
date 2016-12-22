#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: ormdemo.py
@time: 21.12.2016 14:13
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref

# 1. create connection
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/test?charset=utf8',echo = True)

# 2. define mapping
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(100))

    def __str__(self):
        return "User(id={0}, name={1}, address={2})".format(self.id, self.name,self.address)

# 3.create table
Base.metadata.create_all(engine)

# 4. create session
Session = sessionmaker(engine)
session = Session()

# 5. database manipulation

# u1 = User(name='Zhangsan',address='Beijing')
# # id = NONE
# print u1.id
#
#
# session.add(u1)
# session.commit()
# # id = 1
# print u1.id

# us = [
#     ('lisi1', 'abc'),
#     ('lisi2', 'abc'),
#     ('lisi3', 'abc'),
#     ('lisi4', 'abc'),
#     ('lisi5', 'abc'),
# ]
# for u in us:
#     u2 = User(name = u[0],address=u[1])
#     session.add(u2)
# session.commit()

u1 = session.query(User).filter(User.name.like('li%')).all()
for u in u1:
    print u
    print u.name

u1 = session.query(User).filter(User.name == 'Zhangsan').first()
print u1

u1.address = 'Jilin'
session.commit()

session.delete(u1)
session.commit()