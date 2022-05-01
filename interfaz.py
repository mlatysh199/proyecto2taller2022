# La base de la interfaz gráfica.
import pygame
from random import randint


# Colores
rojo = (255, 100, 10)
morado = (100, 100, 255)


# Explicación: Determina si dos vecinos son iguales.
# Dominio: La matriz, una posición en la matriz y la posición de referencia.
# Codiminio: Verdadero o Falso.
def comparar(matriz, i, j, x, y):
    if x == len(matriz) or y == len(matriz[0]):
        return False
    return matriz[i][j] == matriz[x][y]


# Explicación: Pone texto sobre la pestaña.
# Dominio: El texto, color, posición, fuente y el display.
# Codominio: Ninguno (cambia la pantalla).
def texto(msg, color, pos, fuente, display):
    textSurf = fuente.render(msg, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (pos[0]), (pos[1])
    display.blit(textSurf, textRect)


# Explicación: El corazón de la interfaz gráfica.
# Dominio: La matriz que se estaría dibujando.
# Codominio: Ninguno (cambia la pantalla).
def gameLoop(matriz):
    ancho, altura = 400, 400
    FPS = 30
    # Código para pygame.
    # ----
    pygame.init()
    gameDisplay = pygame.display.set_mode((ancho, altura))
    pygame.display.set_caption('Resolvedor de Katamino')
    fuente = pygame.font.SysFont('arial', 18)
    clock = pygame.time.Clock()
    # ----
    # Más colores.
    colores = []
    for i in range(32, 127):
        color = (randint(50, 255), randint(50, 255), randint(50, 255))
        while color in colores:
            color = (randint(3, 12)*20 + 15, randint(3, 12)*20 + 15, randint(3, 12)*20 + 15)
        colores.append(color)
    run = True
    # Para el posicionamiento correcto del texto.
    offsetx = 0
    offsety = 0
    calt = int(altura*0.05)
    canch = int(ancho*0.05)
    while run:
        for event in pygame.event.get():
            # Si el usuario quiere cerrar la pestaña.
            if event.type == pygame.QUIT:
              pygame.quit()
              return
            if event.type == pygame.KEYDOWN:
                # Por si la matriz no cabe en la pestaña.
                if event.key == pygame.K_w and 30*(len(matriz) - 1) + offsety > 0:
                    offsety -= 30
                    gameDisplay.fill((0, 0, 0))
                if event.key == pygame.K_a and 30*(len(matriz[0]) - 1) + offsetx > 0:
                    offsetx -= 30
                    gameDisplay.fill((0, 0, 0))
                if event.key == pygame.K_s and offsety + 60 < altura - 3*calt:
                    offsety += 30
                    gameDisplay.fill((0, 0, 0))
                if event.key == pygame.K_d and offsetx + 60 < ancho:
                    offsetx += 30
                    gameDisplay.fill((0, 0, 0))
                if event.key == pygame.K_r:
                    offsetx, offsety = 0, 0
                    gameDisplay.fill((0, 0, 0))
        # Se dibuja la solución.
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                color = colores[matriz[i][j] - 32]
                if comparar(matriz, i, j, i, j + 1):
                    pygame.draw.line(gameDisplay, color, (j*30 + 12 + canch + offsetx, i*30 + calt + offsety), ((j + 1)*30 - 10 + canch + offsetx, i*30 + calt + offsety), 10)
                if comparar(matriz, i, j, i + 1, j):
                    pygame.draw.line(gameDisplay, color, (j*30 + canch + offsetx, i*30 + 12 + calt + offsety), (j*30 + canch + offsetx, (i + 1)*30 - 10 + calt + offsety), 10)
                texto(chr(matriz[i][j]), rojo, (canch + j*30 + 1 + offsetx, calt + i*30 + offsety), fuente, gameDisplay)
                pygame.draw.rect(gameDisplay, color, [j*30 + canch - 10 + offsetx, i*30 + calt - 10 + offsety, 22, 22], 2)
        # Se dibuja tento informativo.
        pygame.draw.rect(gameDisplay, morado, pygame.Rect(0, altura - 3*calt, ancho, 3*calt))
        texto("W, A, S, D y R respectivamente lo mueven", rojo, (ancho//2, altura*0.9), fuente, gameDisplay)
        texto("arriba, izquierda, abajo, derecha y al origen.", rojo, (ancho//2, altura*0.95), fuente, gameDisplay)
        # Código obligatorio de pygame.
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


# Para pruebas.
if __name__ == "__main__":
    matriz = [[35, 38, 38, 42, 42, 42], [35, 38, 38, 38, 37, 42], [35, 35, 37, 37, 37, 42], [35, 61, 61, 61, 37, 43], [61, 61, 43, 43, 43, 43]]
    gameLoop(matriz)
