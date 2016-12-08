#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: weekday.py
@time: 08.12.2016 15:14
"""


def isLeap(year):
    if year % 400 == 0:
        return True
    else:
        if year%4 == 0 and year % 100 != 0:
            return True
        else:
            return False


def dayInMonth(year, month):
    if month == 2:
        if isLeap(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 0


def date(year, month):
    sum_days = 0
    if year < 1900 or year > 9999:
        print 'this is not a valid year'
    else:
        if month < 1 or month > 12:
            print 'this is not a valid moth'
        else:
            for i in range(1900, year):
                if isLeap(i):
                    sum_days += 366
                else:
                    sum_days += 365
            for i in range(1, month+1):
                sum_days += dayInMonth(year,i)
            return sum_days % 7
    return -1


print date(1901,1)
print date(1960,5)
print date(2000,2)
print date(2016,12)
print date(2000,13)
print date(1800, 2)