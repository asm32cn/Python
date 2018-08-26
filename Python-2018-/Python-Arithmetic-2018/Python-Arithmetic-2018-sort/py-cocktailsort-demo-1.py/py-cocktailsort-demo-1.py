#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-cocktailsort-demo-1.py

class CocktailSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])

    def Swap(self, data, i, j):
        data[i], data[j] = data[j], data[i]

    def CocktailSort(self, data):
        left = 0
        right = len(data) - 1
        while left < right:
            for i in xrange(left, right):
                if data[i] > data[i + 1]:
                    self.Swap(data, i, i + 1)
            right -= 1
            for i in xrange(right, left, -1):
                if data[i - 1] > data[i]:
                    self.Swap(data, i - 1, i)
            left += 1

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    csd = CocktailSortDemo1()
    csd.DisplayData(data)
    csd.CocktailSort(data)
    csd.DisplayData(data)
