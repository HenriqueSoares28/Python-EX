import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021c.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Da pra escutar? ')