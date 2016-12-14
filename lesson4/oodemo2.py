#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: oodemo2.py
@time: 13.12.2016 17:17
"""

class Person(object):
    pass


class Chinese(Person):
    """
    author: jingyang
    """
    nation = 'China'

    #instructor. self must be the first parameter.
    # this is a private method
    def __init__(self, id, name, age, sex):
        #public property
        self.name = name
        #private property. but accessible from external by name(just tell the user, this is a private property)
        self._age = age
        #private property. not accessible from external by name, because name is changed by python
        self.__sex = sex
        self.__id = id
        self.__income = 0;

    def __str__(self):
        return self.name + self.__sex

    # this is a public method
    def getSex(self):
        return self.__sex

    def setSex(self,sex):
        if sex=='m' or sex=='f':
            self.__sex = sex
    # define how to read the property
    @property
    def Age(self):
        return self._age

    # set property  propertyName.setter
    @Age.setter
    def Age(self, age):
        self._age = age

    @property
    def Income(self):
        return self.__income

    @Income.setter
    def Income(self, income):
        self.__income = income

    def __add__(self, other):
        self.Income = self.Income + other
        return self

    # less than
    def __lt__(self, other):
        return self.Age < other.Age


    #@Age.deleter delete the property

    # this is a class method, will be bound on the class
    # the first parameter is cls
    @classmethod
    def test(cls):
        if cls.Age > 18:
            return True
        else:
            return False


    # class method can be used by overloading, which is not supported by Python
    @classmethod
    def getPeopleByParent(cls,parent):
        return cls(id, name, age, sex)

    # this is a static method
    # donot need any self or cls
    @staticmethod
    def isChinese():
        pass








# create object. that call the __init__ implicit. do not need to pass self parameter
a = Chinese('zhangsan',20,'m')

print a.name
# can be used.
print a._age
#can not be found. private member
# print a.__sex

# dir is used to find all members in the object
# __sex is changed to _Chinese__sex. so we can access the sex with the new name
print dir(a)

a._Chinese__sex = 'f'
# this calls __str__ function of a
print a

print a.getSex()

print a.Age
a.Age = 10
print a.Age
