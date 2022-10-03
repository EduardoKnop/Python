# Aula Módulos
# Este programa reproduzirá um áudio .mp3
# Autor: Eduardo Knop

import pygame

pygame.mixer.init()     # Iniciando o Mixer
pygame.init()           # Iniciando o PyGame   **Tem que ser nessa ordem**

pygame.mixer.music.load('Mario.mp3')
pygame.mixer.music.play()
pygame.event.wait()
