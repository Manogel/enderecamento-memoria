from math import* 
from cache import Cache
from random import* 
class Memoria:
	Lista = list()
	ApenasEnderecos = list()
	def __init__(mem, x):
		mem.bits = int(x)
		mem.numEnd = int(pow(2,mem.getBits()))
		mem.ListaEnderecos()

	def ListaEnderecos(mem):
		y = str()
		for x in range(mem.getNumEnd()):
			y = bin(x).split('0b')[1]
			while (len(y) != mem.getBits()):
				y = '0' + y
			k = []
			k.append(y)
			k.append(str(randint(0, 100))+'sdd'+str(randint(0, 100)))
			mem.setLista(k)
				
	def Listagem(mem):
		aux = '|'+'ENDERECO'.center(10)+'|'+'DADO'.center(10)+'|'
		for x, y in Memoria.Lista:
			aux += '\n|'+f'{x}'.center(10)+'|'+f'{y}'.center(10)+'|'
		print(aux)
			
	def setLista(mem, x):
		mem.getLista().append(x)
		mem.getEnderecos().append(x[0])
		
	def getLista(mem):
		return Memoria.Lista	
		
	def getBits(mem):
		return mem.bits
	
	def getNumEnd(mem):
		return mem.numEnd
		
	def getEnderecos(mem):
		return mem.ApenasEnderecos
	
			
