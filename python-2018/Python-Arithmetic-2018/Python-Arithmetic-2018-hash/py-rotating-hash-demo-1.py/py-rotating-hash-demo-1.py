#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-rotating-hash-demo-1.py

class PyRotatingHashDemo1():
	def RotatingHash(self, s, nPrime):
		n = len(s)
		nHash = n
		for i in xrange(n):
			nHash = (nHash << 4 >> 28) ^ ord(s[i])
		return nHash % nPrime

if __name__ == '__main__':
	A_strKeys = ("C", "C++", "Java", "C#", "Python", "Go", "Scala", "vb.net", "JavaScript", "PHP", "Perl", "Ruby")
	prhd = PyRotatingHashDemo1()

	for i in xrange(len(A_strKeys)):
		print '%-10d %-15s %3d' % (i, A_strKeys[i], prhd.RotatingHash(A_strKeys[i], 31))

'''
0          C                 5
1          C++              12
2          Java              4
3          C#                4
4          Python           17
5          Go               18
6          Scala             4
7          vb.net           23
8          JavaScript       23
9          PHP              18
10         Perl             15
11         Ruby             28
'''