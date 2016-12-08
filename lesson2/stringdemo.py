#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: stringdemo.py
@time: 07.12.2016 15:11
"""

# a String is just like a tulpe
# a String can be defined with ' '  " " or ''' '''
x = 'hello world'
print x[0]

y = x+'s'
print y

z = 'hello \'world\' '
u = "hello 'world'"
j = 'hello "world"'

k = ''' 'hello' "world" '''

print z *3
print u
print j
print k

list = ['hello', 'world','python']

print ' '.join(list)
print ','.join(list)