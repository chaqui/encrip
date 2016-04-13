# -*- coding: utf-8 -*-
class  CaracterCantidad():
	"""docstring for  CaracterCantidad"""
	def agregarValores(self,car,cant):
		self.caracter=car
		self.cantidad=cant
		
class Nodo():
	"""docstring for nodo"""
	def __init__(self):
		self.bandera=0
		self.visitado=False
	def agregarHijoIzq(self,nodo):
		self.nodoIzq=nodo
		self.nodoIzq.bandera=1
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
			print "caracter hijo Izq: "+str(listaX[0].contenido.caracter)
			x=2
			y=0
			self.nuevaLista=[]
			insertadoNodo = False
			if(len(listaX)==2):
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
									print "q"
									print len(listaX)
									self.nuevaLista.insert(len(listaX),nodo)
									insertadoNodo = True
								print y
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
	def recorrerArbol(self,nodo,x):
		try:
			print str(x) +chr(nodo.contenido.caracter)+str(nodo.contenido.cantidad)
		except:
			print str(x) + str(nodo.contenido.caracter) + str(nodo.contenido.cantidad)
		x=x+1
		try:
			print "izquierdo"
			if(nodoizq.visitado==False):
				self.recorrerArbol(nodo.nodoIzq,x)
			try:
				if (nodoizq.visitado == False):
					print "derecho"
					self.recorrerArbol(nodo.nodoDer, x)
			except AttributeError, e:
				return None
		except AttributeError, e:
			try:
				print "derecho"
				self.recorrerArbol(nodo.nodoDer, x)
			except AttributeError, e:
				return None
	def recorrerArbol1(self):
		print "arbol"
		#print str(self.lista[0].nodoIzq.contenido.caracter)
		self.recorrerArbol(self.lista[0],1)

class Algoritmo():
	def crearPila(self):
		self.pila = Pila()
		self.pila.crearLista()
	def recorrerCadena(self,cadena):
		for caracter in cadena:
			self.convertirElemento(caracter)
		self.pila.imprimirLista()
		self.pila.ordenar()
		self.pila.imprimirLista()
		self.pila.crearArbol()
		self.pila.recorrerArbol1()
	def convertirElemento(self,letra):
		letra2= int(ord(letra))
		self.pila.insertarElemento(letra2)

cadena = raw_input('Introduce una cadena de texto: ')
algoritmo = Algoritmo()
algoritmo.crearPila()
algoritmo.recorrerCadena(cadena)




