#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: funcdemo4.py
@time: 08.12.2016 13:43
"""

x = [1,2,3,5]


# call function parameter by reference. x will be modified
def f(a):
    a[2] = 'hello world'


f(x)
print x