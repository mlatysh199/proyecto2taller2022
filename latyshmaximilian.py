# Para este proyecto no fue empleada la recursion en si. Por lo
# - tanto, no se considera necesario establecer el limite de
# - recursion.
# Importamos a la biblioteca sys y con este definimos el limite de 
# - recursión como 2^31-1 dado que este es el límite de recursión
# - más grande en python.
#import sys
#sys.setrecursionlimit((1 << 31) - 1)


# Lista que guarda las rotaciones de cada pieza en forma ordenada en una sublista.
# Se asume que cada pieza tiene 8 rotaciones.
rotaciones = []


# Explicación: Convierte un pedazo recibido de cada pieza en una lista de
# - Falso y valores de caracteres en términos de ASCII
# Dominio: Vacío
# Codominio: Una lista de 4 valores numéricos.
# Nota: Se tiene que notar que se puede hacer una versión por compresión
# - pero se dice que no hace falta hacerlo más pequeño ya.
def convertirPedazo():
	pedazo = list(input())
	for i in range(4):
		if pedazo[i] == ".":
			pedazo[i] = False
		else:
			# ord() y chr() son procesos opuestos.
			pedazo[i] = ord(pedazo[i])
	return pedazo


# Explicación: Recorta la pieza con diferentes modos.
# Dominio: La pieza (una matriz de valores naturales) y las dos banderas
# - que determinan el modo.
# Codominio: Vacío (cambia la pieza en sí).
# Nota: Funciona incluso para piezas disconexas...
# foc es "fila o columna"
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


# Explicación: Recorta cada pieza.
# Dominio: La pieza (una matriz de valores naturales).
# Codominio: Vacío (se cambia la pieza en sí).
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


# Explicación: Maneja el recibimiento de cada pieza.
# Dominio: Vacío (se basa del stdin).
# Codominio: La pieza (una matriz de valores naturales).
def recibirPieza():
	pieza = [convertirPedazo() for i in range(4)]
	recortarPieza(pieza)
	return pieza


# Explicación: Determina el tamaño de una matriz a partir de los valores
# - mayores a 0.
# Dominio: Una matriz de valores numéricos.
# Codominio: Un valor natural.
# Tenemos que asegurarnos de que si la pieza es válida tomando la suma
# - total de todas las piezas y viendo si es igual a las dimensiones.
def tamanoMatriz(matriz):
	tamano = 0
	for fila in matriz:
		for i in fila:
			tamano += i > 0
	return tamano


# Explicación: Determina si hay suficientes piezas para llenar la tabla.
# Dominio: Las piezas (una lista de matrices de valores naturales) y las
# - dimensiones de la tabla.
# Codominio: Verdad o Falso.
def esPosible(piezas, L, A):
	total = 0
	for i in piezas:
		total += tamanoMatriz(i)
	return total >= L*A and L > 0 and A > 0


# Explicación: 
# Dominio: 
# Codominio: 
# Antonio y Ariel
def rotacion90(pieza):
	pass


# Explicación: 
# Dominio: 
# Codominio: 
# Antonio y Ariel
def rotacionInvertir(pieza):
	# [[1, 2, 3]] -> [[3, 2, 1]]
	pass


# Explicación: 
# Dominio: 
# Codominio: 
# Antonio y Ariel
# Tiene que modificar la lista "rotaciones". Es decir, para cada
# - pieza se tiene que guardar sus respectivas rotaciones NO repetetidas.
# Nota: Las piezas son guardadas de forma ordenada.
def crearRotaciones(piezas):
	# temporal
	for i in piezas:
		subrotaciones = [i]
		rotaciones.append(subrotaciones)


# Explicación: Determina si un estado es una solución.
# Dominio: Una matriz de valores numéricos representante de la tabla.
# Codominio: Verdad o Falso.
def esSolucion(mesa):
	return tamanoMatriz(mesa) == len(mesa)*len(mesa[0])


# Explicación: Encuentra el "primer" campo que sea Falso.
# Dominio: Una matriz de valores numéricos representante de la tabla.
# Codominio: Un par de valores naturales o None.
def encontrarPrimeroDisponible(mesa):
	for i in range(0, len(mesa)):
		for j in range(0, len(mesa[0])):
			if not mesa[i][j]:
				return [i, j]
	return [-1, -1]


# Explicación: Encuentra la posición respectiva del primer valor que no
# - sea Falso en la primera fila de una rotación dada de una pieza.
# Dominio: Una matrizde valores numéricos representante de una rotación
# - dada de una pieza.
# Codominio: Un valor natural (aunque tomando en cuentra las limitaciones
# - del enunciado del proyecto se puede decir que es de 0 a 3).
def encontrarDesplazamiento(pieza):
	for i in range(len(pieza[0])):
		if pieza[0][i]:
			return i


# Explicación: Duplica una matriz con un nuevo id.
# Dominio: Una matriz.
# Codominio: Una matriz.
# Nota: Se pensaria que este es un metodo redundante, pero no.
# - Python simplemente no logra manejar bien su memoria.
# - Es decir, da referencia a valores guardados incluso con
# - matriz.copy() (no aplica .copy() a las sublistas!!!).
def clonarMatriz(matriz):
	clon = []
	for i in matriz:
		clon.append([])
		for j in i:
			clon[-1].append(j)
	return clon
		

# Explicación: Intenta meter una pieza adentro de una mesa dada.
# Dominio: Una matriz representante de la tabla, una matriz representate 
# - de la pieza, un par de naturales y un número entero.
# Codominio: Falso si no lo logra meter y sino la mesa con la pieza metida.
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


# Explicación: Encuentra los hijos de un tablero (con la premisa de la pila).
# Dominio: Una lista que contiene una matriz y una sublista y una matriz.
# Codominio: Una lista de listas que contienen una matriz y una sublista
# - cada una.
def encontrarHijos(madre, piezas):
	hijos = []
	posicionref = encontrarPrimeroDisponible(madre[0])
	if not (posicionref[0] + 1):
		return hijos
	for i in range(len(piezas)):
		if i not in madre[1]:
			for j in rotaciones[i]:
				# madre[0].copy() no funciona para el caso dado.
				intento = intentarMeterPieza(clonarMatriz(madre[0]), j, posicionref, encontrarDesplazamiento(j))
				if intento:
					hijos.append([intento, madre[1] + [i]])
	return hijos


# Explicación: El solucionador del katamino a principio de la pila.
# Dominio: Una lista de matrices representantes de las piezas de katamino
# - y dos números naturales 
# Codominio: None si no hay solución y sino una matriz de valores naturales
# - representante de la solución.
def pila(piezas, L, A):
	# Se hubiera utilizado [[False]*A]*L pero este crea fuerzas spooky entre
	# - elementos que no se deberian relacionarse.
	pila = [[[[False]*A for i in range(L)], []]]
	while pila:
		ultimo = pila.pop()
		if esSolucion(ultimo[0]):
			return ultimo[0]
		pila = pila + encontrarHijos(ultimo, piezas)


# Explicación: Imprime una matriz recibida aplicando chr.
# Dominio: Una matriz con valores ASCII.
# Codominio: Vacio (imprime la matriz.)
def imprimirMatriz(matriz):
	for i in matriz:
		print(*map(chr, i), sep = "")
	

# Explicación: Función principal que activa el programa.
# Dominio: Vacío (recibe un stdin).
# Codominio: Vacío (imprime los resultados).
def main():
	info = [int(i) for i in input().split(" ")]
	piezas = [recibirPieza() for i in range(info[2])]
	#for i in piezas:
	#	imprimirMatriz(i)
	#	print()
	if not esPosible(piezas, info[0], info[1]):
		print("No hay respuesta!")
		return
	crearRotaciones(piezas)
	resultado = pila(piezas, info[0], info[1])
	if resultado:
		imprimirMatriz(resultado)
	else:
		print("No hay respuesta!")


if __name__ == "__main__":
	main()
