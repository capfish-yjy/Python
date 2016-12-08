#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: embedfuncdemo.py
@time: 08.12.2016 14:59
"""


def outer():
    print 'in outer function'

    def inner():
        print 'in inner function'
    return inner


x = outer()
x()

outer()()