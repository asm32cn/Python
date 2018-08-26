#!/usr/bin/enn python
# -*- coding: utf-8 -*-

# Python 2.7
# py-merge-sort-demo-1.py

class MergeSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    
    def Merge(self, data, left, mid, right):
        n = right - left + 1
        temp = [0] * n
        index = 0
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            index += 1
            i += 1
        while j <= right:
            temp[index] = data[j]
            index += 1
            j += 1
        for k in xrange(n):
            data[left] = temp[k]
            left += 1
    
    # 递归实现的归并排序(自顶向下)
    def MergeSortRecursion(self, data, left, right):
        # 当待排序的序列长度为1时，递归开始回溯，进行merge操作
        if left == right:
            return

        mid = (left + right) / 2
        self.MergeSortRecursion(data, left, mid)
        self.MergeSortRecursion(data, mid + 1, right)
        self.Merge(data, left, mid, right)
    
    def MergeSortIteration(self, data):
        # 子数组索引，前一个为A[left ... mid]，后一个为A[mid + 1 ... right]
        n = len(data)
        i, left, mid, right = 1, 0, 0, 0
        # 子数组的大小i初始为1，没轮翻倍
        while i < n:
            left = 0
            # 后一个子数组存在(需要归并)
            while left + i < n:
                mid = left + i - 1
                # 后一个子数组大小可能不够
                right = (mid + i) if (mid + i < n) else (n - 1)
                self.Merge(data, left, mid, right)
                # 前一个子数组索引向后移动
                left = right + 1

            i *= 2

if __name__ == '__main__':
    data1 = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    data2 = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]


    msd = MergeSortDemo1()

    msd.DisplayData(data1)
    msd.MergeSortRecursion(data1, 0, len(data1) - 1)
    msd.DisplayData(data1)

    print
    msd.DisplayData(data2)
    msd.MergeSortIteration(data2)
    msd.DisplayData(data2)
