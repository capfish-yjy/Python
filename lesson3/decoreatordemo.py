#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: decoreatordemo.py
@time: 08.12.2016 15:07
"""


def authorize(funcname):

    def wrapper(*args, **kwargs):
        username = raw_input('username :')
        password = raw_input('password :')
        if username == 'zhang' and password == '1234':
            return funcname(*args,**kwargs)
        else:
            print 'request not allowed'
    return wrapper


def search(keyword):
    print 'user search product '+ str(keyword)


def order(itemid):
    print 'user order item '+ str(itemid)

@authorize
def pay(orderid):
    print 'user buy order '+ str(orderid)


order(1234)

pay(1234)
