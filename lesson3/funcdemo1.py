#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: funcdemo1.py
@time: 08.12.2016 13:11
"""


def __handleHtml(html):
    print html


def __handelText(text):
    print  text


def __handelJson(json):
    print json


def decoder(type):
    if type =='html':
        return __handleHtml
    if type == 'text':
        return __handelText
    else:
        return __handelJson


decoder('html')('<p>this is a html text</p>')
