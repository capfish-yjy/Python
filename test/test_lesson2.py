#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: test_lesson2.py
@time: 04.12.2016 12:11
"""
import unittest
from lesson2.mysort import mysort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
        print('final:', mysort(testlist))
        self.assertEqual(mysort(testlist), [2, 4, 8, 13, 14, 26, 27, 28, 33, 35], 'test failed')



if __name__ == '__main__':
    unittest.main()
