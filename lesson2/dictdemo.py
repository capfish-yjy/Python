#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: dictdemo.py
@time: 07.12.2016 16:15
"""

x = [1,2,3,4,5]
y = '12345'

# a list is not hashable, so you can not use a list as the key of a dictionary entry
# print hash(x)
print hash(y)

# create a dictionary
z= {'name':'zhang', 'age':30, 'sex':'m'}

print z

z = dict(name='zhang',age = 30, sex = 'm')

print z
print z['name']

# there is no loc key. throw exception
# print z['loc']

# test if loc is a key in dict
print 'loc' in z

for (k,v) in z.items():
    print str(k) + '=' + str(v)

print z.keys()
print z.values()

print z.get('name')

#if loc ist not in the key set, return a defined value 'None'
print z.get('loc',None)

# if key in dic, return it's value. if key not in dic, add the entry with the given value 'China'
z.setdefault('loc', 'China')
print z.get('loc')

m = {'abc':1, 'def':2}

# add m to z
z.update(m)
print z


n = {'name':'yu'}
#if the key is already exist, update the value of the key
z.update(n)

print z