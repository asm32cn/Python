# py-sort-tiobe-filename-demo-1.py

import re

def Main():
	A_strFiles = (
		'TIOBE Index for April 2018.html',
		'TIOBE Index for February 2018.html',
		'TIOBE Index for January 2018.html',
		'TIOBE Index for June 2018.html',
		'TIOBE Index for March 2018.html',
		'TIOBE Index for May 2018.html',
		'TIOBE-exchange-matrix-data.html',
		'TIOBE-exchange-matrix-data.py',
		'TIOBE-gernate-index-py2.py',
		'TIOBE-index.html',
		'TIOBE_matrixData.txt')

	A_strSorted = sort_tiobe_filename_demo(A_strFiles)

	print '%-2s %-36s %-36s' % ('@', 'Source data', 'Sorted data')
	print '%-2s %-36s %-36s' % ('==', '==================', '==================')
	for i in xrange(len(A_strFiles)):
		print '%2d %-36s %-36s' % (i, A_strFiles[i], A_strSorted[i])

def sort_tiobe_filename_demo(data):
	_month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
		'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

	nCount = len(data)

	_regex = re.compile('^TIOBE Index for (\w+) (\d{4})\.html$')
	# buff = [[i, 0] for i in xrange(nCount)]
	buff = []
	n = [0]
	def incN():
		n[0] += 1
		return n[0]

	for i in xrange(nCount):
		m = _regex.findall(data[i])
		# buff[i][1] = int(m[0][1]) * 100 + (_month[m[0][0]]) if m else incN()
		buff.append([i, (int(m[0][1]) * 100 + (_month[m[0][0]]) if m else incN())])

	def takeSecond(el):
		return el[1]

	buff.sort(key=takeSecond)

	_list = []
	for i in xrange(nCount):
		# print buff[i]
		_list.append(data[buff[i][0]])

	return _list

if __name__ == '__main__':
	Main();