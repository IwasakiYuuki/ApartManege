#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, Qt

from openpyxl import *


class Waterservice(QWidget):
	def __init__(self,*indLists):
		super().__init__()
		self.lists = indLists
		self.num = len(self.lists)
		self.text = self.num*[0]
		self.beforeValue = self.num*[0]
		self.afterValue = self.num*[0]
		self.okButton = None
		self.canButton = None
		self.createUI()
		self.show()

	def createUI(self):

		vbox = self.createShishin(*self.lists)
		hbox = self.createOkCancel()
		vbox.addLayout(hbox)
		vbox.setContentsMargins(10,10,10,0)
		
		self.setGeometry(300,300,250,200)
		self.setLayout(vbox)


	def createShishin(self,*lists):

		hbox = self.num*[0]
		vbox = QVBoxLayout()
		hbox_thum = QHBoxLayout()
		label1 = QLabel('前回指針',self)
		label2 = QLabel('今回指針',self)
		hbox_thum.addStretch(3)
		hbox_thum.addWidget(label1,5)
		hbox_thum.addStretch(2)
		hbox_thum.addWidget(label2,5)
		vbox.addLayout(hbox_thum,1)
		
		for n, div in enumerate(self.lists):
			hbox[n] = QHBoxLayout()
			self.text[n] = QLabel(str(div[1]),self)
			hbox[n].addWidget(self.text[n],2)
			self.beforeValue[n] = QLineEdit(self)
			hbox[n].addWidget(self.beforeValue[n],5)
			buf = QLabel('〜',self)
			hbox[n].addWidget(buf,1)
			self.afterValue[n] = QLineEdit(self)
			hbox[n].addWidget(self.afterValue[n],5)
			print(str(n)+':'+str(div))
			
			vbox.addLayout(hbox[n],1)

		return vbox


	def	createOkCancel(self):

		hbox = QHBoxLayout()
		hbox.addStretch(1)

		self.okButton = self.createButton('OK',QCoreApplication.instance().quit,exp = '実行')	#コールバック関数待ち
		self.canButton = self.createButton('Cancel',QCoreApplication.instance().quit,exp = 'キャンセル')
		
		hbox.addWidget(self.okButton)
		hbox.addWidget(self.canButton)
		hbox.setSpacing(10)
		hbox.setAlignment(Qt.AlignRight)
		hbox.setContentsMargins(0,0,0,0)

		return hbox


	def createButton(self,text,callback,exp=None):
		
		btn = QPushButton(text)
		btn.clicked.connect(callback)

		if(exp!=None):
			btn.setToolTip(exp)
		
		btn.resize(btn.sizeHint())

		return btn


	def closeEvent(self,event):

		reply = QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	

class ExcelManage(object):
	
	def __init__(self):
		self.indConf = None
		

	def readConf(self,filepath,sheetName):

		wb = load_workbook(filePath)
		ws = wb.get_sheet_by_name(sheetName)

		lists = ws.rows

		for row in lists:
			self.indConf.append(row)


	def	createTemplate(self):

		





if __name__ == '__main__':
	
	lists = [(1,'ああ'),(2,'いい'),(3,'うう'),(4,'ええ')]
	app = QApplication(sys.argv)
	water = Waterservice(*lists)
	sys.exit(app.exec_())


