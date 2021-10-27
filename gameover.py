import pygame, sys, os, time
import creditsTxt as txt 

pygame.init()
screen = pygame.display.set_mode((640,512))
run = True
FPS = 100
fpsClock = pygame.time.Clock()

GAMEOVER = pygame.image.load(os.path.join("data", "gej_ower.png")).convert()

screen.blit(GAMEOVER, (0,0))
pygame.display.flip()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                exec(open('menu.py').read())
            elif event.key == pygame.K_ESCAPE:
                run = False
    
    fpsClock.tick(FPS)
