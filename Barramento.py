from math import *
from Memoria import Memoria
from cache import Cache
class Barramento:
	hit = 0
	miss = 0
	Cache = list()
	def __init__(bar, x):
		bar.Memoria = Memoria(x)
		bar.setCache()
		pass
		
	def MapearEndereco(bar, bit):
		x = str(bit)
		while len(x) != bar.Memoria.getBits():
			x = '0' + x		

		if (len(x)<=0 or len(x) > bar.Memoria.getBits() or x not in bar.Memoria.getEnderecos()):
			print('Valor invalido')
			return 

			
		aux = ceil(log(bar.Memoria.getBits(), 2))
		num = int ('0b' + x,2)
		indice = x[-aux:]
		aux2 = '0b'+indice
		niv = int(aux2, 2)
		tag = x[:-aux]
		if (Barramento.Cache[niv].MapearCache(tag, indice, bar.Memoria.getLista()[num][1])):
			Barramento.hit += 1
		else:
			Barramento.miss += 1
				
	def MostraEnderecos(bar):
		bar.Memoria.Listagem();
		print("#$#$#$#$#$#$#$#$#$#$#$#$#")
		
	def setCache(bar):
		x = ceil(log(bar.Memoria.getBits(),2))
		y = int(pow(2,x))
		temp = list()
		t = ''
		for c in range(y):
			t = bin(c).split('0b')[1]
			while len(t) != x:
				t = '0' + t
			temp.append(t)
		for n, v in enumerate(temp):
			bar.AlocaCache(n, v)
		print('************'.center(10))
		print(f'Foi gerado {len(Barramento.Cache)} linhas de cache!!')
		print('************'.center(10))

	def AlocaCache(bar, nivel, indice):
		l = Cache(nivel, indice)
		Barramento.Cache.append(l)
	
	def getHit(bar):
		return Barramento.hit
	def getMiss(bar):
		return Barramento.miss
	def getCache(bar):
		return Barramento.Cache
		
		
		
	
		
	
