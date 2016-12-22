#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: homework.py
@time: 22.12.2016 09:58
"""

from mysql import connector

# create connection
params = dict(host ='localhost',port=3306, user='root', password='root', database='test')
conn = connector.connect(**params)

# create cursor
cursor = conn.cursor()

sqltemplate = """
    insert into ip(ip_start,ip_end,nation,provider) values(%s, %s, %s, %s)
"""

myfile = open('2014ips_cut.txt', 'r')
line = myfile.readline()
while line:
    list = line.split()
    try:
        ip_start = list[0]
    except IndexError:
        ip_start = ''

    try:
        ip_end = list[1]
    except IndexError:
        ip_end = ''

    try:
        nation = list[2]
    except IndexError:
        nation = ''

    try:
        provider = list[3]
    except IndexError:
        provider = ''

    print(ip_start + ' : ' + ip_end + ' : ' + nation + ' : ' + provider)
    u = (ip_start, ip_end, nation, provider)
    cursor.execute(sqltemplate,u)
    conn.commit()
    line = myfile.readline()
myfile.close()
conn.close()



