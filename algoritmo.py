# -*- coding: utf-8 -*-
#Descripcion de los variables que tiene cada nodo
import binario as binario


class  CaracterCantidad():
	"""docstring for  CaracterCantidad"""
	def agregarValores(self,car,cant):
		#caracter que almacena el nodo
		self.caracter=car
		#cantidad de caraccreres
		self.cantidad=cant


class Retorno():

	def agregarValores(self,nodo,caracter, binario):
		self.nodo=nodo
		self.caracter=caracter
		self.binario=binario


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
			print nodo.bandera
			try:
				print "caracter hijo Izq: "+chr(listaX[0].contenido.caracter)
			except:
				print "caracter hijo Izq: " + str(listaX[0].contenido.caracter)
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

	def recorrerArbol(self,nodo,x,binario):
		retorno=Retorno()
		nNodo=nodo
		hijoIzqVisitado=False
		hijoDerVisitado=False
		try:
			print "try"
			print str(x) +chr(nodo.contenido.caracter)+str(nodo.contenido.cantidad)
			self.binario = binario + str(nodo.bandera)
			print self.binario
		except:
			print "EXCEPT"
			print str(x) + str(nodo.contenido.caracter) + str(nodo.contenido.cantidad)
			self.binario = binario + str(nodo.bandera)
		x=x+1
		try:
			if(nodo.nodoizq.visitado==False):
				self.binario=binario+str(nodo.contenido.bandera)
				print "izquierdo"
				regreso= self.recorrerArbol(nodo.nodoIzq,x+1,self.binario)
			else:
				nNodo.hijoIzqVisitado=True
			try:
				if(nodo.nodoDer.visitado==False):
					print "derecho"
					regreso=self.recorrerArbol(nodo.nodoDer, x+1,self.binario)
				else:
					nNodo.hijoDerVisitado=True
			except:
				nNodo.hijoDerVisitado=True
		except:
			nNodo.hijoIzqVisitado=True

		try:
			if(nodo.nodoDer.visitado==False):
				print "derecho"
				self.retorno=self.recorrerArbol(nodo.nodoDer, x+1,self.binario)
			else:
				nNodo.hijoDerVisitado=True
		except AttributeError, e:
			nNodo.hijoDerVisitado=True
		if(nodo.contenido.caracter!="vacio"):
			retorno.caracter=nodo.contenido.caracter
			nNodo.visitado=True
			retorno.binario=self.binario
		if (hijoDerVisitado == True and hijoIzqVisitado == True):
			nNodo.visitado = True
		retorno.nodo=nNodo
		return retorno


	def recorrerArbol1(self):
		print "arbol"
		self.recorrerArbol(self.lista[0],1,"")

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




