from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
from cache import*

class Int_Cache(QWidget):
	BOXMAIOR = QHBoxLayout()
	Box = QHBoxLayout()
	box = QVBoxLayout()
	boxDados = QVBoxLayout()
	def __init__(self, cache, parent=None):
		super(Int_Cache, self).__init__(parent)
		#Int_Cache.BOXMAIOR.addLayout(Int_Cache.box)
		self.cache = cache
		self.Escopo()
		#self.roldana = QScrollBar()
		#self.roldana.setMaximum(10)
		#Int_Cache.BOXMAIOR.addWidget(self.roldana)
		#self.roldana.sliderMoved.connect(self.sliderval)
	
	def vizualizar(self):
		self.ok.clicked.connect(self.close)
		self.setLayout(Int_Cache.box)
		
		
	def Escopo(self):
		Int_Cache.Box.addWidget(QLabel('INDICE'.center(15)))
		Int_Cache.Box.addSpacing(20)
		Int_Cache.Box.addWidget(QLabel('VALIDADE'.center(15)))
		Int_Cache.Box.addSpacing(50)
		Int_Cache.Box.addWidget(QLabel('TAG'.center(15)))
		Int_Cache.Box.addSpacing(50)
		Int_Cache.Box.addWidget(QLabel('DADO'.center(15)))
		Int_Cache.box.addLayout(Int_Cache.Box)
		
	def attDados(self, nova):
		self.LimparLayout(Int_Cache.boxDados)
		self.cache = nova
		self.LinhasBox = list()
		for x in self.cache:
			BoxAux = QHBoxLayout()
			BoxAux.addWidget(QLabel(x.getIndice().center(15)))
			BoxAux.addSpacing(50)
			BoxAux.addWidget(QLabel(str(x.getValidade()).center(15)))
			BoxAux.addSpacing(50)
			BoxAux.addWidget(QLabel(x.getTag().center(15)))
			BoxAux.addSpacing(50)
			BoxAux.addWidget(QLabel(x.getDado().center(15)))
			self.LinhasBox.append(BoxAux)
		self.AdicionaDados()
		Int_Cache.box.addLayout(Int_Cache.boxDados)
		self.ok = QPushButton('OK', self)
		Int_Cache.boxDados.addWidget(self.ok)
		self.vizualizar()
		
		
	def AdicionaDados(self):
		for y in self.LinhasBox:
			Int_Cache.boxDados.addLayout(y)		

	def LimparLayout(self, layout):
		'''
		Este foi um codigo tirado do site http://josbalcaen.com/maya-python-pyqt-delete-all-widgets-in-a-layout/
		'''
		while layout.count():
			child = layout.takeAt(0)
			if child.widget() is not None:
				child.widget().deleteLater()
			elif child.layout() is not None:
				self.LimparLayout(child.layout())

	
'''if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = Int_Cache(None)
	app.show()
	root.exec_()'''
