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
