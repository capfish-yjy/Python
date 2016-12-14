#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: oodemo1.py
@time: 13.12.2016 16:55
"""

# this is a classical class fo python.
class Dog:
    pass


# this is a  new class in python
# DogNew extends from object
class DogNew(object):
    pass

# the DogA is extends from a classical class. So this is also a classical class
class DogA(Dog):
    pass

# the DogA is extends from a new class. So this is also a new class
class DogB(DogNew):
    pass


print type(Dog)
print type(DogNew)
print type(DogA)
print type(DogB)
a = Dog()
print a