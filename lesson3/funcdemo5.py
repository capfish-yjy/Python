#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: funcdemo5.py
@time: 08.12.2016 14:03
"""

def f(a, b, c):
    # this is the doc of a function. auto generated
    """
    this function is a test function
    :param a: int
    :param b: bool
    :param c: string
    :return: something
    """
    return a+b+c

f.author = 'yu'
f.createtime = 'today'

print f.author, f.createtime
print f.__doc__
