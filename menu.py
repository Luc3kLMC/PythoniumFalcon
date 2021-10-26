import pygame, sys, os, time
import variables as v

pygame.init()
screen = pygame.display.set_mode((640,512))
run = True
FPS = 30
fpsClock = pygame.time.Clock()

MENU = pygame.image.load(os.path.join("data", "title.png")).convert()

screen.blit(MENU, (0,0))
pygame.display.flip()

while run:
    
    for event in pygame.event.get():
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                v.gameStartProc = True
                exec(open('d8.py').read())
            elif event.key == pygame.K_c:
                exec(open('credits.py').read())
            elif event.key == pygame.K_i:
                exec(open('intro.py').read())
            elif event.key == pygame.K_ESCAPE:
                run = False
    
    if event.type == pygame.QUIT:
            run = False
        
fpsClock.tick(FPS)