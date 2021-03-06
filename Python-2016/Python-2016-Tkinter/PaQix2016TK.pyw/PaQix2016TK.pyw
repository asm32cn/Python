#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaQix2016TK.pyw

from Tkinter import *
from threading import Timer
import random
import time

conf__nCount = 100

class PaQixDef():
	def __init__(self):
		self.x = [0, 0, 0, 0]
		self.y = [0, 0, 0, 0]
		self.dx = [0, 0, 0, 0]
		self.dy = [0, 0, 0, 0]
		self.cr = self.cg = self.cb = 255
		self.dr = self.dg = self.db = 5
	def Config(self, nClientWidth, nClientHeight):
		self.m_nClientWidth  = nClientWidth
		self.m_nClientHeight = nClientHeight
	def Init(self):
		for i in range(2):
			self.x[i] = random.randint(0, self.m_nClientWidth)
			self.y[i] = random.randint(0, self.m_nClientHeight)
			self.dx[i] = random.randint(2, 5)
			self.dy[i] = random.randint(2, 5)
		self.cr = random.randint(0, 255)
		self.cg = random.randint(0, 255)
		self.cb = random.randint(0, 255)
	def Update(self, isUpdate):
		for i in range(2):
			if isUpdate:
				from1 = i
				to1 = i + 2
			else:
				from1 = i + 2
				to1 = i
			self.x[to1] = self.x[from1]
			self.y[to1] = self.y[from1]
			self.dx[to1] = self.dx[from1]
			self.dy[to1] = self.dy[from1]
	def Move(self):
		for i in range(2):
			nx = self.x[i] + self.dx[i]
			if (self.dx[i]>0) and (nx>self.m_nClientWidth) or (self.dx[i]<0) and (nx<0):
				self.dx[i] = -self.dx[i]
			else:
				self.x[i] = nx
			ny = self.y[i] + self.dy[i]
			if (self.dy[i]>0) and (ny>self.m_nClientHeight) or (self.dy[i]<0) and (ny<0):
				self.dy[i] = -self.dy[i]
			else:
				self.y[i] = ny
	def NextColor(self):
		nb = self.cb + self.db
		if (self.db>0 and nb>255) or (self.db<0 and nb<0):
			self.db = -self.db
			ng = self.cg + self.dg
			if (self.dg>0 and ng>255) or (self.dg<0 and ng<0):
				self.dg = -self.dg
				nr = self.cr + self.dr
				if (self.dr>0 and nr>255) or (self.dr<0 and nr<0):
					self.dr = -self.dr
				else:
					self.cr = nr
			else:
				self.cg = ng
		else:
			self.cb = nb

class PaQix2016TK(Tk):
	def __init__(self):
		Tk.__init__(self, None)

		m_nTimerInterval = 0.1
		self.m_nClientWidth, self.m_nClientHeight = 600, 450
		self.m_isRunning = True

		self.pqs = PaQixDef()

		self.title('PaQix2016TK.py')

		self.objCanvas = Canvas(self, width=self.m_nClientWidth, height=self.m_nClientHeight, bg='#000000', bd=0)
		self.objCanvas.pack(expand=YES, fill=BOTH)

		self.A_lines = [None for i in xrange(conf__nCount)]
		self.objCanvas.delete('all')
		for i in range(conf__nCount):
			self.A_lines[i] = self.objCanvas.create_line(0, 0, 1, 1)

		self.DoInit()
		self.DoPaint()

		self.objThread = Timer(m_nTimerInterval, self.OnTimer)
		self.objThread.start()

		self.bind('<Button-1>', self.OnLButtonDown)
		self.bind('<Configure>', self.OnResize)
		self.protocol('WM_DELETE_WINDOW', self.OnDestroy)

	def DoInit(self):
		self.pqs.Config(self.m_nClientWidth, self.m_nClientHeight)
		self.pqs.Init()

	def DoPaint(self):
		try:
			for i in range(conf__nCount):
				if i==5:
					self.pqs.Update(True)
				s1 = 1.0 * i / conf__nCount
				m_strColor = '#%02X%02X%02X' % (self.pqs.cr * s1, self.pqs.cg * s1, self.pqs.cb * s1)
				self.objCanvas.itemconfig(self.A_lines[i], fill=m_strColor)
				self.objCanvas.coords(self.A_lines[i], (self.pqs.x[0], self.pqs.y[0], self.pqs.x[1], self.pqs.y[1]))
				self.pqs.Move()
			self.pqs.NextColor()
			self.pqs.Update(False)
		except:
			#print 'Exception.'
			pass

	def OnLButtonDown(self, event):
		self.DoInit()

	def OnTimer(self):
		while self.m_isRunning:
			time.sleep(0.02)
			self.DoPaint()

	def OnDestroy(self):
		self.m_isRunning = False
		self.objThread.join()
		self.destroy()
		print 'Destroy.'

	def OnResize(self, event):
		if(event.width!=self.m_nClientWidth) or (event.height!=self.m_nClientHeight):
			self.m_nClientWidth = event.width
			self.m_nClientHeight = event.height
			self.DoInit()


if __name__ == '__main__':
	PaQix2016TK()
	mainloop()
