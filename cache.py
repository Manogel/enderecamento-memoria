from math import* 
class Cache:
	def __init__(cache, x, y):
		cache.nivel = x
		cache.validade = False
		cache.indice = y
		cache.tag = str()
		cache.dado = str()	
	
	def MapearCache(cache, tag, indice, dado):
		if (cache.VerificaTag(tag) and cache.VerificaValidade()):
			return True
		else:
			cache.setValidade()
			cache.setTag(tag)
			cache.setDado(dado)
			return False
		
	def setValidade(cache):
		cache.validade = True
	def setTag(cache, x):
		cache.tag = x
	def setDado(cache, x):
		cache.dado = x
	def setIndice(cache, x):
		cache.indice = x
	def setNivel(cache, x):
		cache.Nivel = x
		
	def getValidade(cache):
		return cache.validade
	def getTag(cache):
		return cache.tag
	def getDado(cache):
		return cache.dado
	def getNivel(cache):
		return cache.nivel
	def getIndice(cache):
		return cache.indice
		
	def VerificaValidade(cache):
		if (cache.validade == True):
			return True
	def VerificaIndice(cache, x):
		if (cache.indice == x):
			return True
	def VerificaTag(cache, x):
		if (cache.tag == x):
			return True
		
	
	
