from PyQt4.QtGui import*
from PyQt4.QtCore import*
from Barramento import*
import sys
from IntCache import*
class MemoriaCache(QWidget):
	def __init__(self, x, parent=None):
		super(MemoriaCache, self).__init__(parent)
		self.tamanho = int(x)
		self.Bar = Barramento(x)		
		self.AdministraBox()
		self.SetarBoxEnderecamento()
		self.SetarBoxCache()
		self.SetarBoxStatus()
		self.SetarBotaoVizualizarEnderecos()
		self.Main()
			
	def SetarBotaoVizualizarEnderecos(self):
		self.butaoVerEnd = QPushButton('Vizualizar Enderecos', self)
		self.boxV.addWidget(self.butaoVerEnd)

	def AdministraBox(self):
		self.boxAux = QVBoxLayout()
		self.box = QHBoxLayout()
		self.boxAux.addLayout(self.box)
		
	def Main(self):
		self.bit = self.txtbit.text()
		self.setLayout(self.boxAux)
		self.instanciaAbaCache()
		self.butaoCache.clicked.connect(lambda : self.AbaCache())
		self.butaoE.clicked.connect(lambda : self.setar(bit = self.txtbit.text()))
		self.butaoVerEnd.clicked.connect(lambda : self.Bar.MostraEnderecos())

	def SetarBoxEnderecamento(self):
		self.boxE = QVBoxLayout() #Box de Endereçamento
		self.txt = QLabel('Enderecar Memoria: ')
		self.boxE.addWidget(self.txt)
		self.txtbit = QLineEdit('')
		#texto = QLineEdit.setText(bit)
		self.boxE.addWidget(self.txtbit)
		self.butaoE = QPushButton('Enderecar', self)
		self.boxE.addWidget(self.butaoE)
		self.box.addLayout(self.boxE)	
		
	def SetarBoxStatus(self):
		self.boxV = QVBoxLayout()
		self.boxM = QHBoxLayout()
		self.boxV.addLayout(self.boxM)
		self.box.addSpacing(40)#Adiciona um espaço vertical
		self.box.addLayout(self.boxV)
		self.boxh = QVBoxLayout() #Box Mostra Hits
		self.SetarLedHits()
		self.SetarLedMiss()
		
	def SetarLedHits(self):
		self.hit = QLCDNumber(1)
		self.hit.setSegmentStyle(2)
		self.txthit = QLabel("Hit's: ")
		self.boxh.addWidget(self.txthit)
		self.boxh.addWidget(self.hit)
		self.boxh.addStretch()
		self.boxM.addLayout(self.boxh)
	
	def SetarLedMiss(self):
		self.boxm = QVBoxLayout()
		self.boxM.addSpacing(20)
		self.miss = QLCDNumber(1)
		self.miss.setSegmentStyle(2)
		self.txtmiss = QLabel("Miss's: ")
		self.boxm.addWidget(self.txtmiss)
		self.boxm.addWidget(self.miss)
		self.boxm.addStretch()
		self.boxM.addLayout(self.boxm)
		
	def SetarBoxCache(self):
		self.butaoCache = QPushButton('Vizualizar Cache', self)
		self.boxAux.addWidget(self.butaoCache)		
		
	def setar(self, bit):
		if bit[0] in ['1', '0'] and len(bit) <= self.tamanho:
			self.Bar.MapearEndereco(bit)
			self.miss.display(self.Bar.getMiss())
			self.hit.display(self.Bar.getHit())
		else:
			print('Informe um endereço valido!!')
		
	def AbaCache(self):
		self.abaa.attDados(self.Bar.getCache())
		self.abaa.show()
		pass
	
	def instanciaAbaCache(self):
		self.abaa = None
		self.abaas = None
		self.abaa = Int_Cache(self.Bar.getCache())
		self.abaas = list()
		self.abaas.append(self.abaa)


		

			
'''if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = MemoriaCache(None)
	app.show()
	root.exec_()'''
