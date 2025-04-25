import pygame
import sys
import random

# Colores (no cambiamos tus variables)
azulcielo =(29, 128, 216)
pasto =(38, 175, 22)
asfalto = (111, 122, 110)
anden= (59, 70, 58)
asfalto2 = (255, 255, 0)
edificio1 = (50, 47, 43)
edificio2 = (100, 100, 100)
blanco = (255,255,255)
vidas = 3
pygame.init()
pygame.mixer.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((600,700))
pygame.display.set_caption("play")
clock = pygame.time.Clock()
#cofiguracion de sonido de fondo

ambiente = pygame.mixer.music.load("sound/ambiente2.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)
# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(azulcielo)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad = 3

    def update(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

# Clase para los carros con tamaños y colores aleatorios
class carros(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Tamaño aleatorio entre 50x25 y 80x40
        ancho = random.randint(50, 80)
        alto = random.randint(25, 40)
        
        # Color aleatorio
        coloraleatorio = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(coloraleatorio)
        
        # Posición inicial aleatoria y velocidad
        self.rect = self.image.get_rect()
        
        # Decide en qué carril aparecerá (superior o inferior)
        self.carril = random.choice([0, 1])
        
        if self.carril == 0:
            self.rect.topleft = (-100, 255)  # Carril superior (de izquierda a derecha)
            self.velocidad = random.randint(2, 6)  # Velocidad aleatoria
        else:
            self.rect.topright = (700, 440)  # Carril inferior (de derecha a izquierda)
            self.velocidad = -random.randint(2, 6)  # Velocidad negativa para mover de derecha a izquierda

    def update(self):
        # Actualiza la posición de los carros
        self.rect.x += self.velocidad
        
        # Si el carro se sale de la pantalla, vuelve a aparecer al otro lado
        if self.carril == 0 and self.rect.x > 650:  # Carril superior
            self.rect.x = -100
        elif self.carril == 1 and self.rect.x < -300:  # Carril inferior
            self.rect.x = 700

# Creación del jugador
jugador = Jugador(280, 600)

# Grupos de sprites
grupo_jugador = pygame.sprite.Group()
grupo_jugador.add(jugador)

grupo_carros = pygame.sprite.Group()

# Crear varios carros aleatorios
for _ in range(5):  # Cambia el número para más o menos carros
    grupo_carros.add(carros())

# Bucle principal del juego
while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    # Actualizar todos los sprites
    teclas = pygame.key.get_pressed()
    grupo_jugador.update(teclas)
    grupo_carros.update()
    
    # Dibujar el fondo
    ventana.fill(azulcielo)
    
    # Terreno y carretera
    pygame.draw.rect(ventana, pasto, (0, 180, 600, 600))  # Terreno
    pygame.draw.rect(ventana, asfalto, (0, 250, 600, 100))  # Autopista 1
    pygame.draw.rect(ventana, anden, (0, 200, 600, 50))  # Andén
    pygame.draw.rect(ventana, asfalto2, (0, 290, 200, 20))  # Líneas divisorias
    pygame.draw.rect(ventana, asfalto2, (300, 290, 200, 20))
    pygame.draw.rect(ventana, asfalto2, (560, 290, 200, 20))
    
    # Barrera de medio
    pygame.draw.rect(ventana, anden, (0, 350, 600, 100))
    
    # Autopista 2
    pygame.draw.rect(ventana, asfalto, (0, 400, 600, 100))
    pygame.draw.rect(ventana, anden, (0, 500, 600, 50))
    pygame.draw.rect(ventana, asfalto2, (0, 440, 200, 20))
    pygame.draw.rect(ventana, asfalto2, (260, 440, 200, 20))
    pygame.draw.rect(ventana, asfalto2, (520, 440, 170, 20))
    
    # Edificios de fondo
    pygame.draw.rect(ventana, edificio1, (0, 10, 100, 170))
    pygame.draw.rect(ventana, edificio1, (100, 50, 100, 130))
    pygame.draw.rect(ventana, edificio1, (200, 0, 100, 180))
    pygame.draw.rect(ventana, edificio1, (300, 65, 150, 115))
    pygame.draw.rect(ventana, edificio1, (450, 30, 100, 150))
    pygame.draw.rect(ventana, edificio1, (550, 50, 100, 130))
    pygame.draw.rect(ventana, edificio2, (0, 60, 90, 120))
    pygame.draw.rect(ventana, edificio2, (90, 90, 90, 90))
    pygame.draw.rect(ventana, edificio2, (180, 65, 110, 115))
    pygame.draw.rect(ventana, edificio2, (270, 80, 110, 100))
    pygame.draw.rect(ventana, edificio2, (380, 100, 300, 80))
    font = pygame.font.SysFont('Arial', 30)
    
    
    if pygame.sprite.spritecollideany(jugador, grupo_carros):
        vidas -= 1
        
        jugador.rect.topleft = (280, 600)
        if vidas == 0:
            print("¡Colisión! Game Over.")
            sys.exit()
    
        
    # Dibujar los sprites
    texto_vidas = font.render(f'Vidas: {vidas}', True, (255, 255, 255))
    ventana.blit(texto_vidas, (10, 10))  # Posición en la pantalla
    grupo_jugador.draw(ventana)
    grupo_carros.draw(ventana)

    # Actualizar la ventana
    pygame.display.flip()
