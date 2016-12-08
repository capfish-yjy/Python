#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: funcdemo2.py
@time: 08.12.2016 13:25
"""


def add(a, b):
    return a+b


# use * or ** to define multi parameters in function
def add(*args):
    return sum(args)*2


# if more functions have the same name, the last will be called
# python has no override
print add(10, 20)


def multiple(a, b, c):
    return a*b+c


print multiple(10, 20, 30)

# call the function with name of the parameter
print multiple(10, c=20, b=30)


def func(a, b, c):
    return a+b+c

x = [1,2,34]
print func(x[0],x[1],x[2])
print func(*x)

# dict has the same keys with the parameter names
y = {'a':10,'b':20, 'c':30}
print func(y['a'],y['b'],y['c'])
print func(**y)
# add for the keys of the dict
print func(*y)