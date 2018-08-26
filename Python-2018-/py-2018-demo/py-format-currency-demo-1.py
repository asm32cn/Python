#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-format-currency-demo-1.py

def PA_FormatCurrency(s):
	r = s
	try:
		t = str(round(float(s),2))
		lt = len(t)
		print '::', t, lt
		if(lt > 6):
			st = lt % 3
			i, r = st, t[0:st]
			print st, lt - 6, range(st, lt - 6, 3)
			for i in xrange(st, lt - 6, 3):
				if i:
					r += ',';
				r += t[i:i+3]
			print 'i=', i
			r += ',' + t[i:i+6]
		else:
			r = t
	except:
		pass
	return r

def test(s):
	print s, PA_FormatCurrency(s)

test('3.140009');
test('123456.5678');
test('1234567.5678');
test('12345678.5678');
test('123456789.5678');
test('111113');
test('aa');
test(None);
test('');
test('/');

