import pygame, sys
pygame.init()

# Definir colores
BLACK = (0,0,0)
WHITE = (52,63,54)

size = (800, 500)

# Crear ventana
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
    #    print(event)
        if event.type == pygame.QUIT:
            sys.exit()
