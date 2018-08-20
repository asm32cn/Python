#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-selectionsort-demo-1.py

class SelectionSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def SelectionSort(self, data):
        n = len(data)
        for i in xrange(n - 1):
            min = i
            for j in xrange(i + 1, n):
                if data[j] < data[min]:
                    min = j
            if min != i:
                data[min], data[i] = data[i], data[min]

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    ssd = SelectionSortDemo1()
    ssd.DisplayData(data)
    ssd.SelectionSort(data)
    ssd.DisplayData(data)
