# Importamos a la biblioteca sys y con este definimos el limite de 
# - recursión como 2^31-1 dado que este es el límite de recursión
# - más grande en python.
import sys
sys.setrecursionlimit((1 << 31) - 1)

#Cada pieza tiene 8 rotaciones

#Pueden haber piezas invalidas


# ord() y chr() son procesos opuestos.
def convertirPedazo():
	pedazo = list(input())
	for i in range(4):
		if pedazo[i] == ".":
			pedazo[i] = False
		else:
			pedazo[i] = ord(pedazo[i])
	return pedazo

	
def recortarPiezaAuxUp(pieza, foc):
	longitudhoriz = len(pieza[0])*(not foc) + len(pieza)*foc
	longitudverti = len(pieza[0])*(foc) + len(pieza)*(not foc)
	noaparecio = True
	while 0 < longitudhoriz and noaparecio:
		j = 0
		while j < longitudverti and noaparecio:
			if foc:
				noaparecio = not pieza[0][j]
			elif pieza[j][0]:
				noaparecio = False
			j += 1
		if noaparecio:
			if foc:
				pieza.pop(0)
			else:
				for j in range(longitudverti):
					pieza[j].pop(0)
			longitudhoriz -= 1


def recortarPiezaAuxDown(pieza, foc):
	longitudhoriz = len(pieza[0])*(not foc) + len(pieza)*foc
	longitudverti = len(pieza[0])*(foc) + len(pieza)*(not foc)
	i = longitudhoriz - 1
	noaparecio = True
	while i >= 0 and noaparecio:
		j = 0
		while j < longitudverti and noaparecio:
			if foc:
				noaparecio = not pieza[i][j]
			elif pieza[j][i]:
				noaparecio = False
			j += 1
		if noaparecio:
			if foc:
				pieza.pop()
			else:
				for j in range(longitudverti):
					pieza[j].pop()
			i -= 1

# Nota: Ocupamos dos métodos separados porque una funciona para recortar
# - desde arriba hasta abajo y la otra de abajo hasta arriba. Se necesita
# - hacer ambos procesos como no se puede recortar un espacio que
# - define la proporción de una pieza. Por ejemplo: 
# - $$$$
# - ....
# - $$$$
# - $$.$
# - Obviamente no se puede recortar la segunda fila como esto dañaría
# - la proporción de la pieza.
def recortarPieza(pieza):
	recortarPiezaAuxUp(pieza, True)
	recortarPiezaAuxDown(pieza, True)
	recortarPiezaAuxUp(pieza, False)
	recortarPiezaAuxDown(pieza, False)


def recibirPieza():
	pieza = [convertirPedazo() for i in range(4)]
	recortarPieza(pieza)
	return pieza


# Tenemos que asegurarnos de que si la pieza es válida tomando la suma
# - total de todas las piezas y viendo si es igual a las dimensiones.
def tamanoPieza(pieza):
	tamano = 0
	for pedazo in pieza:
		for i in pedazo:
			tamano += i > 0


if __name__ == "__main__":
	info = [int(i) for i in input().split(" ")]
	piezas = [recibirPieza() for i in range(info[2])]
	for i in piezas:
		print(i)
