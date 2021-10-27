import pygame, sys, os, time
import scoreMessage as txt
import variables as v

pygame.init()

FPS = 100
fpsClock = pygame.time.Clock()

run = True
screen = pygame.display.set_mode((640,512))
font = pygame.font.Font("data\\Topaz-8.ttf", 16)
VAMPIRE = pygame.image.load(os.path.join("data", "vampire.png")).convert()
position = 0
vampireScreen = False

screen.fill((0, 85,85))

if (v.amigaMode == 0):
    printing = txt.atari
elif (v.amigaMode == 2):
    printing = txt.amiga

for i in printing:
    blitTxt = font.render(str(i), True, (0,153,153))
    screen.blit(blitTxt, (0,position))
    pygame.display.flip()
    position += 16
    time.sleep(0.01)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and vampireScreen == True:
                exec(open('menu.py').read())
            elif event.key == pygame.K_RETURN and vampireScreen == False:
                vampireScreen = True
                screen.blit(VAMPIRE, (0,0))
                pygame.display.flip()
                time.sleep(1)
            elif event.key == pygame.K_ESCAPE:
                run = False
    
    fpsClock.tick(FPS)