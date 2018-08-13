#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-format-currency-demo-1.py

import re

def FormatCurrency(s):
	r = s
	try:
		f = float(r)
		t = '{:.2f}'.format(-f if f < 0 else f)
		tl = len(t)
		if tl > 6:
			st = tl % 3
			r = t[0:st] + ',' if st	else ''
			for i in xrange(st, tl - 6, 3):
				r += t[i:i + 3] + ','
			r += t[-6:]
		else:
			r = t
		if f < 0: r = '-' + r
	except:
		pass
	return r

def FormatCurrencyEx1(s):
	r = s if type(s) == str else str(s)
	if r and re.findall('^[-]?\\d*(\\.\\d+)?$', r) and not r == '-':
		f = float(r)
		t = '{:.2f}'.format(-f if f < 0 else f)
		tl = len(t)
		if tl > 6:
			ba = ['*'] * ( tl + (tl - 4) / 3 + (1 if f < 0 else 0) )
			st = tl % 3
			pos = 0
			if f < 0: ba[pos] = '-';pos += 1
			for i in xrange(tl):
				if i and i <= tl - 6 and (i - st) % 3 == 0:
					ba[pos] = ',';pos += 1
				ba[pos] = t[i];pos += 1
			r = ''.join(ba);
		else:
			r = t
			if f < 0: r = '-' + r
	return r

def test(s):
	print '%16s %15s %19s %19s' % (s, type(s), FormatCurrency(s), FormatCurrencyEx1(s))

_data = ['3.140009', '123456.5678', '1234567.5678', '-1234567.5678', \
		'12345678.5678', '-12345678.5678', '123456789.5678', '-123456789.5678', \
		'111113', 'aa', False, '', '/', 12345, -12345, \
		12345.678, -12345.678, .123, -.123, '.456', '-.456', \
		'123aaa', '-123aaa', '.123aa', '-.123aa', 0, 0.0, -0.0, '0', '-0', \
		'-', '0xa0', '12345678912.7654', 12345678912.7654]

for i in _data:
	test(i)

'''
        3.140009    <type 'str'>                3.14                3.14
     123456.5678    <type 'str'>          123,456.57          123,456.57
    1234567.5678    <type 'str'>        1,234,567.57        1,234,567.57
   -1234567.5678    <type 'str'>       -1,234,567.57       -1,234,567.57
   12345678.5678    <type 'str'>       12,345,678.57       12,345,678.57
  -12345678.5678    <type 'str'>      -12,345,678.57      -12,345,678.57
  123456789.5678    <type 'str'>      123,456,789.57      123,456,789.57
 -123456789.5678    <type 'str'>     -123,456,789.57     -123,456,789.57
          111113    <type 'str'>          111,113.00          111,113.00
              aa    <type 'str'>                  aa                  aa
           False   <type 'bool'>                0.00               False
                    <type 'str'>
               /    <type 'str'>                   /                   /
           12345    <type 'int'>           12,345.00           12,345.00
          -12345    <type 'int'>          -12,345.00          -12,345.00
       12345.678  <type 'float'>           12,345.68           12,345.68
      -12345.678  <type 'float'>          -12,345.68          -12,345.68
           0.123  <type 'float'>                0.12                0.12
          -0.123  <type 'float'>               -0.12               -0.12
            .456    <type 'str'>                0.46                0.46
           -.456    <type 'str'>               -0.46               -0.46
          123aaa    <type 'str'>              123aaa              123aaa
         -123aaa    <type 'str'>             -123aaa             -123aaa
          .123aa    <type 'str'>              .123aa              .123aa
         -.123aa    <type 'str'>             -.123aa             -.123aa
               0    <type 'int'>                0.00                0.00
             0.0  <type 'float'>                0.00                0.00
            -0.0  <type 'float'>               -0.00               -0.00
               0    <type 'str'>                0.00                0.00
              -0    <type 'str'>               -0.00               -0.00
               -    <type 'str'>                   -                   -
            0xa0    <type 'str'>                0xa0                0xa0
12345678912.7654    <type 'str'>   12,345,678,912.77   12,345,678,912.77
   12345678912.8  <type 'float'>   12,345,678,912.77   12,345,678,912.80
'''
