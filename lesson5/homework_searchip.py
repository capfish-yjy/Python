#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: homework_searchip.py
@time: 22.12.2016 10:31
"""
from mysql import connector

# create connection
params = dict(host ='localhost',port=3306, user='root', password='root', database='test')
conn = connector.connect(**params)

# create cursor
cursor = conn.cursor()

sqlstatement = """
    SELECT * FROM ip WHERE (INET_ATON('1.1.0.13') BETWEEN INET_ATON(ip_start) AND INET_ATON(ip_end));
"""


cursor.execute(sqlstatement)
for row in cursor:
    print row[2] + ' : ' + row[3]

conn.close()