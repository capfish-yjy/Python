#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: funcdemo3.py
@time: 08.12.2016 13:36
"""


def add(*args):
    return sum(args)

print add(10,20,30,50,1,4,5)



def add(**kwargs):
    return sum(kwargs.values())


print add(a=10, b=20, c=30, d=1, e=5)



def add(*args, **kwargs):
    return sum(args)+sum(kwargs.values())

print add(1,3,5,6,8, a=1, b=5, c=6)

