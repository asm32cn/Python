#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-additive-hash-demo-1.py

class PyAdditiveHashDemo1():
	def AdditiveHash(self, s, nPrime):
		n = len(s)
		nHash = n
		for i in xrange(n):
			nHash += ord(s[i])
		return nHash % nPrime

if __name__ == '__main__':
	A_strKeys = ("C", "C++", "Java", "C#", "Python", "Go", "Scala", "vb.net", "JavaScript", "PHP", "Perl", "Ruby")
	pahd = PyAdditiveHashDemo1()

	for i in xrange(len(A_strKeys)):
		print '%-10d %-15s %3d' % (i, A_strKeys[i], pahd.AdditiveHash(A_strKeys[i], 31))

'''
0          C                 6
1          C++               1
2          Java             18
3          C#               11
4          Python           28
5          Go               29
6          Scala            24
7          vb.net            6
8          JavaScript        2
9          PHP              18
10         Perl              4
11         Ruby             19
'''
