#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-radix-sort-demo-1.py

class LsdRedixSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def LsdRedixSort(self, data):
        dn = 3
        k = 10
        n = len(data)
        C = [0] * k

        radix = [1, 1, 10, 100]
        def GetDigit(x, d):
            return (x / radix[d]) % 10

        # LsdRedixSort
        for d in xrange(1, dn):

            # CountingSort
            for i in xrange(k):
                C[i] = 0
            for i in xrange(n):
                C[GetDigit(data[i], d)] += 1
            for i in xrange(1, k):
                C[i] = C[i] + C[i - 1]
            B = [0] * n
            for i in xrange(n - 1, -1, -1):
                dight = GetDigit(data[i], d)
                C[dight] -= 1
                B[C[dight]] = data[i]
            for i in xrange(n):
                data[i] = B[i]

if __name__ == '__main__':
    # data = [41, 67, 34, 0, 69, 24, 78, 58, 62, 64, 5, 45, 81, 27, 61, 91, 95, 42, 27, 36]
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    lrsd = LsdRedixSortDemo1()

    lrsd.DisplayData(data)
    lrsd.LsdRedixSort(data)
    lrsd.DisplayData(data)