import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mover con flechas")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Posición y velocidad
x, y = 100, 100
velocidad = 5
tamaño = 300

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidad
    if keys[pygame.K_RIGHT]:
        x += velocidad
    if keys[pygame.K_UP]:
        y -= velocidad
    if keys[pygame.K_DOWN]:
        y += velocidad

    # Dibujar
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, ROJO, (x, y, tamaño, tamaño))
    pygame.display.flip()
    reloj.tick(60)
