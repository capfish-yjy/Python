#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: test_lesson4.py
@time: 14.12.2016 15:40
"""
import unittest
from lesson4.myVector import MyArray
from lesson4.myVector import Vector


class MyTestCase(unittest.TestCase):
    def test_array(self):
        array = MyArray(5)
        self.assertEqual(5, array.__len__())
        array.__setitem__(0, 1)
        array.__setitem__(1, 2)
        array.__setitem__(2, 3)
        array.__setitem__(3, 4)
        array.__setitem__(4, 5)

        self.assertEqual(4, array.__getitem__(3))
        self.assertEqual(1, array[0])

    def test_vector_add(self):
        v1 = Vector(3)
        v1[0] = 1
        v1[1] = 2
        v1[2] = 3
        v2 = Vector(3)
        v2[0] = 2
        v2[1] = 4
        v2[2] = 6
        v3 = v1+v2
        self.assertEqual(3, v3.__len__())
        self.assertEqual(3, v3[0])
        self.assertEqual(6, v3[1])
        self.assertEqual(9, v3[2])

    def test_vector_mul(self):
        v1 = Vector(3)
        v1[0] = 1
        v1[1] = 2
        v1[2] = 3
        v2 = Vector(3)
        v2[0] = 2
        v2[1] = 4
        v2[2] = 6
        self.assertEqual(28, v1*v2)


if __name__ == '__main__':
    unittest.main()
