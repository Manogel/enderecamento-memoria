#!/usr/bin/env python3

'''
	Este é o meu arquivo principal que dará inicio ao meu programa!!!!
'''


from PyQt4.QtGui import*
from PyQt4.QtCore import*
#from Barramento import*
import sys
from Memoria_Cache import MemoriaCache
class Main(QWidget):
	def __init__(self,parent=None):
		super(Main, self).__init__(parent)
		self.box = QVBoxLayout()
		self.SetarButaoBit()
		self.butaoSetar.clicked.connect( lambda : self.aba2(self.bitt.text()))
		self.abas = list()

	def SetarButaoBit(self):
		self.lay = QFormLayout()
		self.box.addLayout(self.lay)
		self.bitt = QLineEdit()
		self.butaoSetar = QPushButton('Ok', self)
		self.box.addWidget(self.butaoSetar)
		self.lay.addRow('Informe o numero de bit: ', self.bitt)
		self.setLayout(self.box)

	def aba2(self, bit):
		if (int(bit) <= 1 or int(bit) > 10) and int(bit) not in range(2,11):
			print('Não é aceito!!')
		else:
			import os
			os.system('cls' if os.name == 'nt' else 'clear')
			aba = MemoriaCache(bit)
			self.abas.append(aba)
			self.close()
			aba.show()

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = Main(None)
	app.show()
	root.exec_()
