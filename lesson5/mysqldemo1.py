#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: mysqldemo1.py
@time: 21.12.2016 13:22
"""

from mysql import connector

# create connection
params = dict(host ='localhost',port=3306, user='root', password='root', database='test')
conn = connector.connect(**params)

# create cursor
cursor = conn.cursor()


# execute sql
# ddl = """
#     create table users(id integer, name varchar(40), address varchar(100))
# """
# cursor.execute(ddl)

# dml = """
#     insert into users(name,address) values('zhangsan', 'beijing')
# """
# cursor.execute(dml)
# conn.commit()

sqltext = """
    select * from users
"""
cursor.execute(sqltext)
for row in cursor:
    print row

sqltemplate = """
    insert into users(name,address) values(%s, %s)
"""
# u1=('lisi','abc')
#
# cursor.execute(sqltemplate,u1)
# conn.commit()


us = [
    ('lisi1', 'abc'),
    ('lisi2', 'abc'),
    ('lisi3', 'abc'),
    ('lisi4', 'abc'),
    ('lisi5', 'abc'),
]

cursor.executemany(sqltemplate, us)
conn.commit()

#close connection
conn.close