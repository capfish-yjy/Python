#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: myVector.py
@time: 14.12.2016 15:23
"""

"""
1、参考老师上传的资料的 2.1节内容，实现一个一维数组类，要支持下标操作符


2、继承 1的 数组类实现一个向量类，要求支持向量的加法、乘法运算。
"""

import ctypes


class MyArray(object):
    def __init__(self,size):
        assert size > 0
        self.__size = size
        MyArrayType = ctypes.py_object * size
        self.__elements = MyArrayType()

        self.clear(None)

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self)
        return  self.__elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self)
        self.__elements[index]=value

    def clear(self,value):
        for i in range(len(self)):
            self.__elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self.__elements)


class _ArrayIterator:
    def __init__(self, array):
        self._arrayRef = array
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


class Vector(MyArray):
    def __add__(self, other):
        assert self.__len__() == other.__len__()
        v = Vector(self.__len__())
        for i in range(0, self.__len__()):
            v[i] = self[i]+other[i]
        return v

    def __str__(self):
        s=''
        for i in range(len(self)):
            s += str(self.__getitem__(i)) + ','
        end = len(self)*2-1
        return '(' + s[0:end]+')'

    def __mul__(self, other):
        assert self.__len__() == other.__len__()
        s = 0
        for i in range(0, self.__len__()):
            s += self[i] * other[i]
        return s

