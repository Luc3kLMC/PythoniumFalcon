import pygame, sys, os, time
import creditsTxt as txt 

pygame.init()
screen = pygame.display.set_mode((640,512))
run = True

LMC = pygame.image.load(os.path.join("data", "LMC.png")).convert()
ACE = pygame.image.load(os.path.join("data", "ACE.png")).convert()

font = pygame.font.Font("data\\Topaz-8.ttf", 16)
position = 0

def fadeInLMC():
    fadein = pygame.Surface((640, 512))
    fadein = fadein.convert()
    fadein.fill((0,0,0))
    
    for i in range(255):
        fadein.set_alpha(255 - i)
        screen.blit(LMC, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
        time.sleep(0.01)

def fadeOutLMC():
    fadeout = pygame.Surface((640, 512))
    fadeout = fadeout.convert()
    fadeout.fill((0,0,0))
    for i in range(255):
        fadeout.set_alpha(i)
        screen.blit(LMC, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
        time.sleep(0.01)
    
def fadeInACE():
    fadein = pygame.Surface((640, 512))
    fadein = fadein.convert()
    fadein.fill((0,0,0))
    
    for i in range(255):
        fadein.set_alpha(255 - i)
        screen.blit(ACE, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
        time.sleep(0.01)

def fadeOutACE():
    fadeout = pygame.Surface((640, 512))
    fadeout = fadeout.convert()
    fadeout.fill((0,0,0))
    for i in range(255):
        fadeout.set_alpha(i)
        screen.blit(ACE, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
        time.sleep(0.01)

def creditsDisplay():
    global position
    screen.fill((0, 85,85))
    for i in txt.message:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,position))
        pygame.display.flip()
        position += 16
        time.sleep(0.1)
    



fadeInLMC()
fadeOutLMC()
fadeInACE()
fadeOutACE()
creditsDisplay()

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                execfile('d8.py')
            elif event.key == pygame.K_ESCAPE:
                run = False


