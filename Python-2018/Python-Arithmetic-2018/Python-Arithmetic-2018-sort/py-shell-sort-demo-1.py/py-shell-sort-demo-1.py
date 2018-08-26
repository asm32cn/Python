#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-shell-sort-demo-1.py

class ShellSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def ShellSort(self, data):
        n = len(data)
        h = 0
        while h <= n:
            h = 3 * h + 1
        while h >= 1:
            for i in xrange(h, n):
                j = i - h
                get = data[i]
                while j >= 0 and data[j] > get:
                    data[j + h] = data[j]
                    j -= h
                data[j + h] = get
            h = (h - 1) / 3

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    ssd = ShellSortDemo1()
    ssd.DisplayData(data)
    ssd.ShellSort(data)
    ssd.DisplayData(data)
