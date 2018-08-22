#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PaCalculator2016Qt.py

import sys
from PyQt4 import QtGui, QtCore

strBackspace = u'←'

class PaCalculator2016Qt(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		self.setWindowTitle(u'Python Qt 计算器')

		self.strAlphaTable = '0123456789.+-*/'

		self.initUI()

	def initUI(self):
		font = QtGui.QFont('Arial', 16)
		grid = QtGui.QGridLayout()
		#strStyle = 'QWidget { border:1px solid #006699; border-radius:3px; }'
		self.txtDisplay = QtGui.QLineEdit(self)
		self.txtDisplay.setAlignment(QtCore.Qt.AlignRight)
		self.txtDisplay.setFont(font)
		#self.txtDisplay.setStyleSheet(strStyle)
		strButtons = '789*~\\456/C\\123-=\\0.+'
		nRows, nCols = 1, 0
		grid.addWidget(self.txtDisplay, 0, 0, 1, 5)
		for c in strButtons:
			if c=='\\':
				nRows += 1
				nCols = 0
				continue
			nColspan = 2 if c=='0' else 1
			nRowspan = 2 if c=='=' else 1
			if c=='~':c=strBackspace
			objButton = QtGui.QPushButton(c, self)
			objButton.setFont(font)
			if nColspan==1 and nRowspan==1:
				objButton.setFixedSize(50, 50)
			elif c=='=':
				objButton.setFixedWidth(50)
			elif c=='0':
				objButton.setFixedHeight(50)
			objButton.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
			#objButton.setStyleSheet(strStyle)
			self.connect(objButton, QtCore.SIGNAL('clicked()'), self.buttonClick)
			grid.addWidget(objButton, nRows, nCols, nRowspan, nColspan)
			nCols += nColspan

		self.setLayout(grid)

	def buttonClick(self):
		c = unicode(self.sender().text())

		strDisplay_t = str(self.txtDisplay.text())
		if c=='C':
			self.setDisplay('')
		elif c==strBackspace:
			if strDisplay_t:
				self.setDisplay(strDisplay_t[:-1])
		elif c=='=':
			if False in [ch in self.strAlphaTable for ch in strDisplay_t]:	# 防止手动输入的恶意表达式
				self.setDisplay('F')										# 攻击计算机，比如
				return														# open('1.txt','w').write('te')
			try:
				self.setDisplay( str( eval(strDisplay_t) ) )
			except Exception, e:
				self.setDisplay('E')
		elif c in '+-*/' and (not strDisplay_t or strDisplay_t[-1] in '+-*/'):
			pass
		elif c=='.':
			strDisplay_t_len = len(strDisplay_t)
			nFlag = 0
			for i in xrange(strDisplay_t_len):
				ch = strDisplay_t[strDisplay_t_len-i-1]
				if ch == '.':
					nFlag = 2
					break
				elif ch in '0123456789':
					nFlag = 1
				elif ch in '+-*/':
					break

			if nFlag == 0:
				self.setDisplay( strDisplay_t + '0' + c )
			elif nFlag==1:
				self.setDisplay( strDisplay_t + c )
		else:
			self.setDisplay( strDisplay_t + c )
		print self.txtDisplay.text()

	def setDisplay(self, text):
		self.txtDisplay.setText( text )

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	calc = PaCalculator2016Qt()
	calc.show()
	app.exec_()

