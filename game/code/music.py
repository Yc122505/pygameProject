import pygame

def start_bgm():
    pygame.mixer.init()
    pygame.mixer.music.load("../music/bgm.mp3")
    pygame.mixer.music.play(-1,0.0)
