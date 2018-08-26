#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-BKDRHash-demo-1.py

class PythonBKDRHashDemo1():
	def BKDRHash(self, s):
		nSeed = 131 # 31 131 1313 13131 131313 etc
		nHash = 0
		for ch in s:
			nHash = nHash * nHash + ord(ch)
		return nHash & 0x7fffffff

def Main():
	A_strKeys = ("C", "C++", "Java", "C#", "Python", "Go", "Scala", "vb.net", "JavaScript", "PHP", "Perl", "Ruby")
	brd = PythonBKDRHashDemo1()

	for i in xrange(len(A_strKeys)):
		s = A_strKeys[i]
		nHash = brd.BKDRHash(s)
		print '%-10d %-15s %11u %3d' % (i, s, nHash, nHash % 31)

if __name__ == '__main__':
	Main()

'''
0          C                        67   5
1          C++                20539067  17
2          Java             1097690434  26
3          C#                     4524  29
4          Python           1149485422  28
5          Go                     5152   6
6          Scala            1816149386   2
7          vb.net           1196273413  29
8          JavaScript       2102330469  28
9          PHP                41886864   5
10         Perl             1365279333  25
11         Ruby             1956896226  22
'''