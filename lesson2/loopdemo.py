#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: loopdemo.py
@time: 07.12.2016 16:50
"""


x = range(1,10)

for i in x :
    if i == 5:
        break
    print i
# break loop else will not be run.
else:
    print 'hello'

