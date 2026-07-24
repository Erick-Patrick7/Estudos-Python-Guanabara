# Para rodar este código, certifique-se de ter um arquivo de áudio 
# chamado 'ex06.mp3' na mesma pasta deste script.

import pygame
import time

pygame.init()
pygame.mixer.music.load('ex06.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)
