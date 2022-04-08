# Importamos a la biblioteca sys y con este definimos el limite de 
# - recursión como 2^31-1 dado que este es el límite de recursión
# - más grande en python.
import sys
sys.setrecursionlimit((1 << 31) - 1)

#Cada pieza tiene 8 rotaciones

#Pueden haber piezas invalidas.


def recibirPieza():
	pieza, simbolo = convertirPieza()
	recortarPieza(pieza)
	return [pieza, simbolo]
	
	

def convertirPieza():
	simbolo = False
	pieza = []
	for i in range(4):
		fila = list(input())
		j = 0
		while j < 4 and not simbolo:
			if fila[j] != ".":
				simbolo = fila[j]
			j += 1
		pieza.append([j == simbolo for j in fila])
	return pieza, simbolo


def recortarPiezaAux(pieza, foc):
	longitudhoriz = len(pieza[0])*(not foc) + len(pieza)*foc
	longitudverti = len(pieza[0])*(foc) + len(pieza)*(not foc)
	i = 0
	while i < longitudhoriz:
		noaparecio = True
		j = 0
		while j < longitudverti and noaparecio:
			if foc:
				noaparecio = not pieza[i][j]
			elif pieza[j][i]:
				noaparecio = False
			j += 1
		if noaparecio:
			if foc:
				pieza.pop(i)
			else:
				for j in range(longitudverti):
					pieza[j].pop(i)
			longitudhoriz -= 1
		else:
			i += 1


def recortarPieza(pieza):
	recortarPiezaAux(pieza, True)
	recortarPiezaAux(pieza, False)


if __name__ == "__main__":
	info = [int(i) for i in input().split(" ")]
	piezas = [recibirPieza() for i in range(info[2])]
	for i in piezas:
		print(i)
