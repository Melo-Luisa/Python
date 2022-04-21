import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('agora você escuta?')
pygame.event.wait()
