#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: Lesson1.py
@time: 22.11.2016 13:21
"""
#
# sigmoid
# y = 1 / (1 + e^-x)
#

import math


def sigmoid(x):
    try:
        res = 1 / (1 + math.exp(-x))
    except OverflowError:
        res = 0.0
    return res

