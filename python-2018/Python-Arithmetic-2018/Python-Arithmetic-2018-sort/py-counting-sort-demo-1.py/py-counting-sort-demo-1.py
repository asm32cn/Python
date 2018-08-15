#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-counting-sort-demo-1.py

class CountingSortDemo1():
    k = 100
    def __init__(self):
        pass
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def CountingSort(self, data):
        n = len(data)
        C = [0] * self.k
        # for i in xrange(k):
        #     C[i] = 0
        for i in xrange(n):
            C[data[i]] += 1
        for i in xrange(self.k):
            C[i] = C[i] + C[i - 1]
        B = [0] * n
        for i in xrange(n - 1, -1, -1):
            C[data[i]] -= 1
            B[C[data[i]]] = data[i]
        for i in xrange(n):
            data[i] = B[i]
        del C
        del B

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    csd = CountingSortDemo1()
    csd.DisplayData(data)
    csd.CountingSort(data)
    csd.DisplayData(data)