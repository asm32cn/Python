#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-insertion-sort-dichotomy-demo-1.py

class InsertionSortDichotomyDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])

    def InsertionSortDichotomy(self, data):
        for i in xrange(1, len(data)):
            get = data[i]
            left = 0
            right = i - 1
            while left <= right:
                mid = (left + right) / 2
                if data[mid] > get:
                    right = mid - 1
                else:
                    left = mid + 1
            for j in xrange(i - 1, left - 1, -1):
                data[j + 1] = data[j]
            data[left] = get

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    isdd = InsertionSortDichotomyDemo1()
    isdd.DisplayData(data)
    isdd.InsertionSortDichotomy(data)
    isdd.DisplayData(data)
