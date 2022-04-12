# Para este proyecto no fue empleada la recursion en si. Por lo
# - tanto, no se considera necesario establecer el limite de
# - recursion.
# Importamos a la biblioteca sys y con este definimos el limite de 
# - recursión como 2^31-1 dado que este es el límite de recursión
# - más grande en python.
#import sys
#sys.setrecursionlimit((1 << 31) - 1)


# Lista que guarda las rotaciones de cada pieza.
# - Cada pieza se guarda con una llave de id(pieza[i])
# Se asume que cada pieza tiene 8 rotaciones.
rotaciones = dict()


# ord() y chr() son procesos opuestos.
def convertirPedazo():
	pedazo = list(input())
	for i in range(4):
		if pedazo[i] == ".":
			pedazo[i] = False
		else:
			pedazo[i] = ord(pedazo[i])
	return pedazo


# foc es "fila o cola"
# dou es "down o up"
def recortarPiezaAux(pieza, foc, dou):
	longitudhoriz = len(pieza[0])*(not foc) + len(pieza)*foc - dou
	longitudverti = len(pieza[0])*foc + len(pieza)*(not foc)
	noaparecio = True
	i = 0
	while i < longitudverti and noaparecio:
		# que???
		# Se reemplazan los ifs para promover eficiencia.
		noaparecio = not pieza[(not foc)*i + foc*dou*longitudhoriz][foc*i + (not foc)*dou*longitudhoriz]
		i += 1
	while longitudhoriz + dou and noaparecio:
		if foc:
			pieza.pop(dou*longitudhoriz)
		else:
			for j in range(longitudverti):
				pieza[j].pop(dou*longitudhoriz)
		longitudhoriz -= 1
		noaparecio = bool(longitudhoriz + dou)
		i = 0
		while i < longitudverti and noaparecio:
			noaparecio = not pieza[(not foc)*i + foc*dou*longitudhoriz][foc*i + (not foc)*dou*longitudhoriz]
			i += 1


# Nota: Ocupamos un método separado porque funciona para recortar
# - desde arriba hasta abajo y de abajo hasta arriba. Se necesita
# - hacer ambos procesos como no se puede recortar un espacio que
# - define la proporción de una pieza. Por ejemplo: 
# - $$$$
# - ....
# - $$$$
# - $$.$
# - Obviamente no se puede recortar la segunda fila como esto dañaría
# - la proporción de la pieza.
def recortarPieza(pieza):
	recortarPiezaAux(pieza, True, True)
	recortarPiezaAux(pieza, True, False)
	recortarPiezaAux(pieza, False, True)
	recortarPiezaAux(pieza, False, False)


def recibirPieza():
	pieza = [convertirPedazo() for i in range(4)]
	recortarPieza(pieza)
	return pieza


# Tenemos que asegurarnos de que si la pieza es válida tomando la suma
# - total de todas las piezas y viendo si es igual a las dimensiones.
def tamanoMatriz(matriz):
	tamano = 0
	for fila in matriz:
		for i in fila:
			tamano += i > 0
	return tamano


def esPosible(piezas, L, A):
	total = 0
	for i in piezas:
		total += tamanoMatriz(i)
	return total >= L*A


# Antonio y Ariel
def rotacion90(pieza):
	pass


# Antonio y Ariel
def rotacionInvertir(pieza):
	pass


# Antonio y Ariel
# Tiene que modificar el diccionario "rotaciones". Es decir, para cada
# - pieza se tiene que guardar sus respectivas rotaciones NO repetetidas.
# Otra nota, las llaves son id(pieza[i]).
def crearRotaciones(piezas):
	pass


def esSolucion(mesa):
	return tamanoMatriz(mesa) == len(mesa)*len(mesa[0])


def encontrarPrimeroDisponible(mesa):
	for i in range(0, len(mesa)):
		for j in range(0, len(mesa[0])):
			if not mesa[i][j]:
				return [i, j]


def encontrarDesplazamiento(pieza):
	for i in range(len(pieza[0])):
		if pieza[0][i]:
			return i


# Se pensaria que este es un metodo redundante, pero no.
# - Python simplemente no logra manejar bien sus pointers.
# - Es decir, da referencia a valores guardados incluso con
# - lista.copy().
def clonarMatriz(matriz):
	clon = []
	for i in matriz:
		clon.append([])
		for j in i:
			clon[-1].append(j)
	return clon
		


def intentarMeterPieza(mesa, pieza, posicionref, desplazamiento):
	cambio = posicionref[1] - desplazamiento
	if len(mesa) < len(pieza) + posicionref[0] or len(mesa[0]) < len(pieza[0]) + cambio or cambio < 0:
		return False
	for i in range(len(pieza)):
		for j in range(len(pieza[0])):
			if pieza[i][j]:
				if mesa[posicionref[0] + i][cambio + j]:
					return False
				mesa[posicionref[0] + i][cambio + j] = pieza[i][j]
	return mesa


def encontrarHijos(madre, piezas):
	hijos = []
	posicionref = encontrarPrimeroDisponible(madre[0])
	for i in piezas:
		if id(i) not in madre[1]:
			for j in rotaciones[id(i)]:
				# madre[0].copy() no funciona para el caso dado.
				intento = intentarMeterPieza(clonarMatriz(madre[0]), j, posicionref, encontrarDesplazamiento(j))
				if intento:
					hijos.append([intento, madre[1]+[id(i)]])
	return hijos


def pila(piezas, L, A):
	# Se hubiera utilizado [[False]*A]*L pero este crea fuerzas spooky entre
	# - elementos que no se deberian relacionarse.
	pila = [[[[False for j in range(A)] for i in range(L)]] + [[]]]
	while pila:
		ultimo = pila.pop()
		if esSolucion(ultimo[0]):
			return ultimo[0]
		pila = pila + encontrarHijos(ultimo, piezas)
	return


# Ariel
def imprimirMatriz(matriz):
	pass
	

if __name__ == "__main__":
	info = [int(i) for i in input().split(" ")]
	piezas = [recibirPieza() for i in range(info[2])]
	for i in piezas:
		imprimirMatriz(i)
		print()
	if not esPosible(piezas, info[0], info[1]):
		print("No hay respuesta!")
		quit()
	crearRotaciones(piezas)
	resultado = pila(piezas, info[0], info[1])
	if resultado:
		imprimirMatriz(resultado)
	else:
		print("No hay respuesta!")
