# Importamos a la biblioteca sys y con este definimos el limite de 
# - recursión como 2^31-1 dado que este es el límite de recursión
# - más grande en python.
import sys
sys.setrecursionlimit((1 << 31) - 1)


def recibirPieza():
	simbolo = False
	pieza = []
	for i in range(4):
		fila = list(input())
		if not simbolo:
			for j in fila:
				if i != ".":
					simbolo = j
					break
		pieza = pieza + [[j == simbolo for j in fila]]*(simbolo in fila)
	longitud = len(pieza[0])
	contador = 0
	while contador < longitud:
		noaparecio = True
		for i in pieza:
			if i[contador]:
				noaparecio = False
				break
		if noaparecio:
			for i in range(len(pieza)):
				pieza[i].pop(contador)
			longitud -= 1
		else:
			contador += 1
	return [simbolo, pieza]
#Ariel es gay

if __name__ == "__main__":
	info = [int(i) for i in input().split(" ")]
	piezas = [recibirPieza() for i in range(info[2])]
	for i in piezas:
		print(i)

