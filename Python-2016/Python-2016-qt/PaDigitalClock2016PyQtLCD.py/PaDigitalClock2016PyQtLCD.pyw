#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PaDigitalClock2016PyQtLCD.py

import sys, thread, time
from PyQt4 import QtGui, QtCore

class PaDigitalClock2016PyQtLCD(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)

		lcd = QtGui.QLCDNumber(self)
		self.setCentralWidget(lcd)
		lcd.setDigitCount(12)
		lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
		#pal = lcd.palette()
		#pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0,102,153))
		#lcd.setPalette(pal)
		lcd.setStyleSheet('border:none; color:#FF0; background-color: #023')
		self.objLCD = lcd

		self.resize(750, 200)
		self.setWindowTitle('PaDigitalClock2016PyQtLCD.py')

		thread.start_new_thread(self.Do_Display, () )

	def closeEvent(self, event):
		thread.exit()

	def Do_Display(self):
		while True:
			self.objLCD.display(QtCore.QTime.currentTime().toString('HH:mm:ss.zzz'))
			time.sleep(0.005)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	objForm = PaDigitalClock2016PyQtLCD()
	objForm.show()
	sys.exit(app.exec_())
