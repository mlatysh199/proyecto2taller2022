from random import randint, choice


def matrizVacia(n, m, que):
	return [[que]*m for i in range(n)]


def llenado(matriz):
	for i in matriz:
		for j in i:
			if j:
				return True
	return False


def valido(matriz, posf, posc, dx, dy, mdx, mdy, solo):
	bx, by = dx, dy
	direcciones = []
	for i in range(-1, 2, 2):
		if mdx > dx + i >= 0 and mdy > dy >= 0:
			direcciones.append([i, 0])
		if mdx > dx >= 0 and mdy > dy + i >= 0:
			direcciones.append([0, i])
	if solo:
		otro = direcciones.copy()
		este = choice(otro) if len(otro) > 1 else otro[0]
		otro.remove(este)
		cnt = len(otro)
		while cnt and matriz[posf + dx + este[0]][posc + dy + este[1]]:
			este = choice(otro) if len(otro) > 1 else otro[0]
			otro.remove(este)
			cnt -= 1
		if matriz[posf + dx + este[0]][posc + dy + este[1]]:
			bx += este[0]
			by += este[1]
	else:
		seleccion = choice(direcciones)
		bx, by = seleccion[0] + dx, seleccion[1] + dy
	if bx == dx and by == dy:
		seleccion = choice(direcciones)
		bx, by = seleccion[0] + dx, seleccion[1] + dy
	return bx, by


def rotacion90(matriz):
    matriz_nueva = [[] for i in range(len(matriz[0]))]
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matriz_nueva[i].append(matriz[-j - 1][i])
    return matriz_nueva


def rotacionFlip(matriz):
    matriz_nueva = [[] for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz_nueva[i].append(matriz[i][-j - 1])
    return matriz_nueva


def rotar(pieza, flip, rot):
	if flip:
		pieza = rotacionFlip(pieza)
	for i in range(rot):
		pieza = rotacion90(pieza)
	return pieza


def generarPieza(matriz, modos, posf, posc, cantidad):
	base = matrizVacia(4, 4, ".")
	encontrar = False
	modo = chr(randint(33, 687))
	while modo == "." or modo in modos or 160 >= ord(modo) >= 127:
		modo = chr(randint(33, 687))
	dx, dy = 0, 0
	mdx, mdy = min(4, len(matriz) - posf), min(4, len(matriz[0]) - posc)
	for i in range(cantidad):
		if matriz[posf + dx][posc + dy]:
			encontrar = True
			matriz[posf + dx][posc + dy] = False
			base[dx][dy] = modo
			dx, dy = valido(matriz, posf, posc, dx, dy, mdx, mdy, True)
		else:
			dx, dy = valido(matriz, posf, posc, dx, dy, mdx, mdy, False)
	if encontrar:
		modos.append(modo)
		return rotar(base, randint(0,1), randint(0,3))
	return []
	


def guardar(n, m, piezas):
	with open("input.txt", "w") as file:
		file.write(f"{n} {m} {len(piezas)}" + "\n")
		for i in piezas:
			for j in i:
				file.write("".join(j) + "\n")


def main(n, m):
	matriz = matrizVacia(n, m, True)
	piezas = []
	modos = []
	while llenado(matriz):
		for i in range(len(matriz)//2):
			for j in range(len(matriz[0])//2):
				pieza = generarPieza(matriz, modos, i << 1, j << 1, randint(12, 16))
				if pieza:
					piezas.append(pieza)
	guardar(n, m, piezas)


if __name__ == "__main__":
	main(int(input("n -> ")), int(input("m -> ")))
