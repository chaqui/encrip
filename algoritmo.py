# -*- coding: utf-8 -*-
#Descripcion de los variables que tiene cada nodo

class  CaracterCantidad():
	"""docstring for  CaracterCantidad"""
	def agregarValores(self,car,cant):
		#caracter que almacena el nodo
		self.caracter=car
		#cantidad de caraccreres
		self.cantidad=cant


class Llave():
	def __init__(self):
		self.caracter=""
		self.binario=""

	def agregarValores(self,caracter, binario):
		self.caracter=caracter
		self.binario=binario

class Encriptamiento():
	def __init__(self,llave,encriptamiento):
		self.llave = llave
		self.encriptaminto = encriptamiento


class Nodo():
	"""docstring for nodo"""

	def __init__(self):
		self.bandera=1
		self.visitado=False

	def agregarHijoIzq(self,nodo):
		self.nodoIzq=nodo
		self.nodoIzq.bandera=0

	def agregarHijoDer(self,nodo):
		self.nodoDer=nodo

	def AgregarContenido(self, cont):
		self.contenido=cont




class Pila():
	def crearLista(self):
		self.lista=[]
	def insertarElemento(self,caracter):
		i=0
		bandera=False
		for elemento in self.lista:
			if(elemento.contenido.caracter ==caracter):
				bandera=True
				break
			i = i + 1
		if(bandera == False):
			nodo = Nodo()
			cont = CaracterCantidad()
			cont.agregarValores(caracter,1)
			nodo.AgregarContenido(cont)
			self.lista.insert(0,nodo)
		else:
			self.lista[i].contenido.cantidad=self.lista[i].contenido.cantidad+1

	def imprimirLista(self):
			print "pila"
			numero=0
			for	elemento in self.lista:
				print str(numero)+" "+chr(elemento.contenido.caracter)+" "+str(elemento.contenido.cantidad)
				numero= numero + 1

	def ordenar(self):
		self.nuevaLista=[]
		x=0
		for elemento in self.lista:
			x=x+1
			if len(self.nuevaLista)==0:
				self.nuevaLista.insert(0,elemento)
			else:
				y = 0
				for elemento2 in self.nuevaLista:
					if elemento.contenido.cantidad < elemento2.contenido.cantidad:
						self.nuevaLista.insert(y,elemento)
						y = y + 1
						break
					else:
						if(elemento.contenido.cantidad== elemento2.contenido.cantidad):
							if(elemento.contenido.caracter<elemento2.contenido.caracter):
								self.nuevaLista.insert(y,elemento)
								y = y + 1
								break
							else:
								if len(self.nuevaLista) == y + 1:
									self.nuevaLista.append(elemento)
									break
								else:
									y = y + 1
						else:
							if len(self.nuevaLista) == y+1:
								self.nuevaLista.append(elemento)
								break
							else:
								y=y+1
		self.lista=self.nuevaLista

	def crearArbol1(self,listaX,iteracion):
		print "iteracion "+str(iteracion)
		if len(listaX)==1:
			return listaX
		else:
			print str(len(listaX))
			nodo = Nodo()
			nodo.agregarHijoIzq(listaX[0])
			nodo.agregarHijoDer(listaX[1])
			cont = CaracterCantidad()
			cont.agregarValores("vacio", listaX[0].contenido.cantidad+listaX[1].contenido.cantidad)
			nodo.AgregarContenido(cont)
			try:
				print "caracter hijo Izq: "+chr(listaX[0].contenido.caracter)
			except:
				print "caracter hijo Izq: " + str(listaX[0].contenido.caracter)
			x=2
			y=0
			self.nuevaLista=[]
			insertadoNodo = False
			if(len(listaX)==2):
				nodo.bandera=None
				self.nuevaLista.insert(y,nodo)
			else:
				while(x<len(listaX)):
					len(listaX)
					if(insertadoNodo==False):
						if(nodo.contenido.cantidad<listaX[x].contenido.cantidad):
							print "nodo"
							self.nuevaLista.insert(y,nodo)
							y=y+1
							self.nuevaLista.insert(y, listaX[x])
							insertadoNodo= True
						else:
							if(nodo.contenido.cantidad==listaX[x].contenido.cantidad):
								self.nuevaLista.insert(y,nodo)
								y = y + 1
								self.nuevaLista.insert(y, listaX[x])
								insertadoNodo=True
							else:
								if(listaX[len(listaX)-1].contenido.cantidad<nodo.contenido.cantidad):
									self.nuevaLista.insert(len(listaX),nodo)
									insertadoNodo = True
								self.nuevaLista.insert(y,listaX[x])
					else:
						print "caracter"
						self.nuevaLista.insert(y,listaX[x])
					y = y + 1
					x = x + 1
			return self.crearArbol1(self.nuevaLista,iteracion=iteracion+1)

	def crearArbol(self):
		print "crear arbol"
		print str(len(self.lista))
		self.Nlista=self.crearArbol1(self.lista,1)
		self.lista=self.Nlista

	def recorrerArbol(self,nodo,binario):
		print str(nodo.bandera)
		if nodo.bandera!=None:
			binario1 = binario + str(nodo.bandera)
		else:
			binario1 =binario
		if(nodo.contenido.caracter !="vacio"):
			llaveUnica = Llave()
			llaveUnica.agregarValores(nodo.contenido.caracter,binario1)
			self.llave.insert(len(self.llave),llaveUnica)
		else:
			try:
				self.recorrerArbol(nodo.nodoIzq,binario1)
			except:
				pass
			try:
				self.recorrerArbol(nodo.nodoDer,binario1)
			except:
				pass

	def recorrerArbol1(self):
		self.llave=[]
		print "arbol"
		nodoP=self.lista[0]
		self.recorrerArbol(nodoP,"")
		print len(self.llave)
		for x in self.llave:
			print chr(x.caracter)+" "+str(x.binario)

	def convinar(self,cadena):
		self.cadena= cadena
		encriptBinario=""
		for caracter in self.cadena:
			for llave in self.llave:
				if(int(ord(caracter)) == llave.caracter):
					encriptBinario=encriptBinario+llave.binario
		print encriptBinario
		return encriptBinario
class Algoritmo():
	def crearPila(self):
		self.pila = Pila()
		self.pila.crearLista()
	def recorrerCadena(self,cadena):
		self.cadena =cadena

		for caracter in cadena:
			self.convertirElemento(caracter)
		self.pila.imprimirLista()
		self.pila.ordenar()
		self.pila.imprimirLista()
		self.pila.crearArbol()
		self.pila.recorrerArbol1()
		self.encriptadoBinario = self.pila.convinar(cadena)
		print self.encriptadoBinario
		self.crearEncriptamiento()
		encriptado =  Encriptamiento(self.pila.llave,self.encriptadoFull)
		return  encriptado
	def convertirElemento(self,letra):
		letra2= int(ord(letra))
		self.pila.insertarElemento(letra2)
	def crearEncriptamiento(self):
		cadenaBinaria=""
		self.encriptadoFull=""
		a=0
		print a
		for binario in self.encriptadoBinario:
			if(a==0):
				cadenaBinaria=""
				a=a+1
			if(a<8):
				print "d"
				cadenaBinaria=cadenaBinaria+binario
				a=a+1
			else:
				cadenaBinaria = cadenaBinaria + binario
				print "g"
				print cadenaBinaria
				print int(cadenaBinaria,2)
				print chr(int(cadenaBinaria,2))
				self.encriptadoFull=self.encriptadoFull+chr(int(cadenaBinaria,2))
				a=0
		print "p"
		print a
		if (a<8 and a!=0):
			for x in [a, 8]:
				cadenaBinaria=cadenaBinaria+"0"
			print cadenaBinaria
			self.encriptadoFull = self.encriptadoFull + chr(int(cadenaBinaria, 2))
		print "h"
		print self.encriptadoFull

cadena = raw_input('Introduce una cadena de texto: ')
algoritmo = Algoritmo()
algoritmo.crearPila()
encriptamiento = algoritmo.recorrerCadena(cadena)
print chr(210)