#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: test_lesson1.py
@time: 22.11.2016 14:10
"""
import unittest
from Lesson1.Lesson1 import sigmoid
import sys


class MyTestCase(unittest.TestCase):
    def test_sigmoid(self):
        x = 0
        result = sigmoid(x)
        self.assertEqual(result, 0.5, 'test failed')

    def test_sigmoid_big(self):
        x = -10000000
        result = sigmoid(x)
        self.assertEqual(result, 0.0, 'test failed')

    def test_sigmoid_small(self):
        x = 1000000000000000000000000000000000000000000
        result = sigmoid(x)
        self.assertEqual(result, 1.0, 'test failed')




if __name__ == '__main__':
    unittest.main()
