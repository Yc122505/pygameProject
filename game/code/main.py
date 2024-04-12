import pygame
import gif_pygame
import music
#import button

def place_plants(plant, x,y):
    screen.blit(plant.blit_ready(), (x, y))

def get_name(obj):
    for name, value in globals().items():
        if value is obj:
            return name
    return None
    
pygame.init()
pygame.display.set_caption("Plants vs. Zombies")

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
DEFAULT_CARD_SIZE = (50,70)
CARD_BACKGROUND = (70,90)
in_game_background = pygame.image.load('../images/src/interface/background1.jpg')
sunflower = gif_pygame.load('../images/src/Plants/Sunflower/SunFlower.gif')
sunflower_card = pygame.image.load('../images/src/Card/Plants/sunflower.png')
card_background = pygame.image.load('../images/src/Card/Plants/CardBackground.png')

sunflower_card = pygame.transform.scale(sunflower_card, DEFAULT_CARD_SIZE)
card_background = pygame.transform.scale(card_background, CARD_BACKGROUND)

screen = pygame.display.set_mode((1400, 600), pygame.RESIZABLE)

current_selected_plant = sunflower


music.start_bgm()

ocupancy = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()


            for i in range(9):
                for j in range(6):
                    if  (335+(i*80) >= x >= 255+(i*80)) and \
                            (175+(j*95) >= y >= 80+(j*95)):
                        ocupancy.append([255+i*80,80+j*95, current_selected_plant])

    screen.blit(in_game_background, (0, 0))
    screen.blit(card_background, (0, 0))
    for i in ocupancy:
        screen.blit(i[2].blit_ready(), (i[0], i[1]))

    pygame.display.update()


    

pygame.quit()
