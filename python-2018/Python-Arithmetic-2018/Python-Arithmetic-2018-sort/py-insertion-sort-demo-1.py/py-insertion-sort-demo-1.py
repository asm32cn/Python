#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-insertion-sort-demo-1.py

class InsertionSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def InsertionSort(self, data):
        for i in xrange(1, len(data)):
            get = data[i]
            j = i - 1
            while j >= 0 and data[j] > get:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = get

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    isd = InsertionSortDemo1()
    isd.DisplayData(data)
    isd.InsertionSort(data)
    isd.DisplayData(data)
