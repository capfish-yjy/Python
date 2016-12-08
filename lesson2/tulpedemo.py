#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: tulpedemo.py
@time: 07.12.2016 15:06
"""

#tulpe's size and content can not be modified
x = (1,3,5)

print x[0], x[2]

# x[0] =100 is not permitted


# multiple return value of a function
# the return value is put in a tuple
def add(x,y):
    return x,y, x+y


print add(10,20)
#result is a tulpe
result = add(10,20)
print add(10,20)[0],result[1],result[2]

# use multiple vars to save the return value of the function
x,y,z = add(30,40)
print x,y,z