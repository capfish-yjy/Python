#! /usr/bin/python
# encoding: utf-8

"""
@author: Jingyang
@contact:
@file: countWords.py
@time: 04.12.2016 13:23
"""

#Takes a list and returns a descending sorted dict of words and their counts


def countWords(a_list):
    words = {}
    for i in range(len(a_list)):
        item = a_list[i]
        count = a_list.count(item)
        words[item] = count
    return sorted(words.items(), key = lambda item: item[1], reverse=True)

print(countWords("the quick red fox jumped over the lazy brown dog".split()))