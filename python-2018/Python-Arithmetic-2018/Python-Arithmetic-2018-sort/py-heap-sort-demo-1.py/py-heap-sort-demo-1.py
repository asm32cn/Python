#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-heap-sort-demo-1.py

class HeapSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])

    def Heapify(self, data, i, size):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        max = i
        if left_child < size and data[left_child] > data[max]:
            max = left_child
        if right_child < size and data[right_child] > data[max]:
            max = right_child
        if max != i:
            data[i], data[max] = data[max], data[i]
            self.Heapify(data, max, size)

    def HeapSort(self, data):
        # BuildHeap
        heap_size = len(data)
        for i in xrange(heap_size / 2 - 1, -1, -1):
            self.Heapify(data, i, heap_size)

        # HeapSort
        while heap_size > 1:
            heap_size -= 1
            data[0], data[heap_size] = data[heap_size], data[0]
            self.Heapify(data, 0, heap_size)

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    hsd = HeapSortDemo1()
    hsd.DisplayData(data)
    hsd.HeapSort(data)
    hsd.DisplayData(data)