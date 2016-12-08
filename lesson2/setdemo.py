#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: setdemo.py
@time: 07.12.2016 16:29
"""

a = set([1,2,3,4,5])

# a frozenset is not changeable. can not add delete change entry in the frozenset
# there is no add function in forzenset
b = frozenset(range(4,11))


print a
print b

c = b|a
# c has the same type as b (frozenset)
print c

print a.isdisjoint(b)


# update and different_update