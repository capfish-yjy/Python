#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: test_lesson3.py
@time: 08.12.2016 15:36
"""
import unittest
from lesson3.weekday import dayInMonth
from lesson3.weekday import isLeap
from lesson3.weekday import date


class MyTestCase(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(True, isLeap(2000))
        self.assertEqual(False, isLeap(1998))
        self.assertEqual(False, isLeap(1900))

    def test_dayinmonth(self):
        self.assertEqual(31, dayInMonth(1998, 12))
        self.assertEqual(28, dayInMonth(1998, 2))
        self.assertEqual(29, dayInMonth(2000, 2))
        self.assertEqual(30, dayInMonth(2000, 4))

    def test_date(self):
        self.assertEqual(4, date(1901, 1))
        self.assertEqual(2, date(1960, 5))
        self.assertEqual(2, date(2000, 2))
        self.assertEqual(6, date(2016, 12))
        self.assertEqual(0, date(2016, 7))
        self.assertEqual(-1, date(2000, 13))


if __name__ == '__main__':
    unittest.main()
