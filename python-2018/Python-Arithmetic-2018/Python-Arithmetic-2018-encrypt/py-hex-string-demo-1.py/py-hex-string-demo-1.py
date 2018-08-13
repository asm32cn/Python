#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-hex-string-demo-1.py

class HexString():
	strHexDigit = "0123456789ABCDEF"
	def HexStringEncode(self, s):
		i, nCount = 0, len(s)
		cache = ['\0'] * (nCount * 2)
		for ch in s:
			nCode = ord(ch)
			cache[i] = self.strHexDigit[(nCode & 0xf0) >> 4]; i += 1;
			cache[i] = self.strHexDigit[nCode & 15]; i += 1;
		return ''.join(cache)

	def HexStringDecode(self, s):
		dict = {}
		for i in xrange(len(self.strHexDigit)):
			dict[self.strHexDigit[i]] = i
		nCount = len(s) / 2
		cache = ['\0'] * nCount
		for i in xrange(nCount):
			n = i + i
			cache[i] = chr( (dict[s[n]] << 4) + dict[s[n + 1]] )
		return ''.join(cache)

def Main():
	hs = HexString()
	strSource = 'py-base64-demo-1.py\n程序中书写着所见所闻所感，编译着心中的万水千山。'
	strEncrypt = hs.HexStringEncode(strSource)
	strDecrypt = hs.HexStringDecode(strEncrypt)
	print 'strSource:\n\t%s\nstrEncrypt:\n\t%s\nstrDecrypt:\n\t%s' % (strSource, strEncrypt, strDecrypt)

if __name__ == '__main__':
	Main()


'''
strSource:
	py-base64-demo-1.py
程序中书写着所见所闻所感，编译着心中的万水千山。
strEncrypt:
	70792D6261736536342D64656D6F2D312E70790AE7A88BE5BA8FE4B8ADE4B9A6E58699E79D80E68980E8A781E68980E997BBE68980E6849FEFBC8CE7BC96E8AF91E79D80E5BF83E4B8ADE79A84E4B887E6B0B4E58D83E5B1B1E38082
strDecrypt:
	py-base64-demo-1.py
程序中书写着所见所闻所感，编译着心中的万水千山。
'''
