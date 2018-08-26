#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-quicksort-demo-1.py

class QuickSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def QuickSort(self, data, left, right):
        if left < right:
            key = data[left]
            low = left
            high = right
            while low < high:
                while low < high and data[high] >= key:
                    high -= 1
                data[low] = data[high]
                while low < high and data[low] <= key:
                    low += 1
                data[high] = data[low]
            data[low] = key

            self.QuickSort(data, left, low - 1)
            self.QuickSort(data, low + 1, right)

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    qsd = QuickSortDemo1()
    qsd.DisplayData(data)
    qsd.QuickSort(data, 0, len(data) - 1)
    qsd.DisplayData(data)