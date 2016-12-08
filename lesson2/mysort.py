#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: Lesson1.py
@time: 22.11.2016 13:21
"""
#bubble sort


def mysort(data):
    """

    :type data: Array
    """
    for j in range(len(data)-1, 0, -1):
        for i in range(0, j):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data




