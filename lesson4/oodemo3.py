#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: oodemo3.py
@time: 14.12.2016 14:12
"""


class A(object):

    def __init__(self):
        pass

    def sayHi(self):
        print 'in A'


class B(A):
    def __init__(self):
        pass


class C(A):
    def __init__(self):
        pass

    def sayHi(self):
        print 'in C'


class D(A):
    def __init__(self):
        pass

    def sayHi(self):
        A.sayHi(self)
        super(D, self).sayHi()
        print 'in D'


class E(D,C):
    def __init__(self):
        pass

    def sayHi(self):
        super(E, self).sayHi()
        print 'in E'


b = B()
b.sayHi()

c = C()
c.sayHi()

d = D()
d.sayHi()

e = E()
e.sayHi()