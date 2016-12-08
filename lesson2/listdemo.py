#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: listdemo.py
@time: 07.12.2016 14:48
"""


x= [1,2,3,4]
y = list()

x.append(5)
y.append(7)
y.append(8)

x.extend(y)
x.extend([8, 'yu'])

del x[0]

print x[0]
print x
print y
print x+y

# copy 3 times x
print x*3

print x[-2]

#default step = 1
z= range(1, 20)

print z

revert = z[::-1]
print revert

#from index[2,100) step=3. the end can be bigger than the length of the list
print z[2:100:3]



test = range(10,20)
for index,value in enumerate(test):
    print index, value

print len(test)

print reversed(test)

test.extend([-5,-18,2,-7,9,-30])
print sorted(test)
print sorted(test, key=abs)

x = range(1,7)

y = [i**2 for i in x]
print y

z = [i**2 if i<3 else i**3 for i in x]

print z


x = range(1,10)
# 生成器，定义了一个方法
y = xrange(1,10)

print x,y

for i in y:
    print y

