#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: legbdemo.py
@time: 08.12.2016 13:48
"""


x = 'global'

def f1():
    x = 'local'
    print x


f1()



def outer():
    x = 'enclose'
    def inner():
        print x
    inner()

outer()



def test():
    def inner():
     # that is wrong  x += 'e'
     # this is right
        global x
        x+='e'
        print x
    inner()

test()