#CARREGANDO ARQUIVO MP3
import pygame

pygame.init()
pygame.mixer.music.load('aula8-exc021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()