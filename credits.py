from variables import STATE_CREDITS
import pygame, sys, os, time
import creditsTxt as txt 
import variables as v

pygame.init()
screen = pygame.display.set_mode((640,512))

LMC = pygame.image.load(os.path.join("data", "LMC.png")).convert()
ACE = pygame.image.load(os.path.join("data", "ACE.png")).convert()

font = pygame.font.Font("data\\Topaz-8.ttf", 16)


def fadeInLMC():
    
    fadein = pygame.Surface((640, 512))
    fadein = fadein.convert()
    if (v.fadeTick < 1):
        fadein.fill((0,0,0))
    elif (v.fadeTick > 0 and v.fadeTick < 255): 
        fadein.set_alpha(255 - v.fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
    elif (v.fadeTick >= 256):
        fadein.set_alpha(v.fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
        v.stateActual = v.STATE_LMC_FADE_OUT
        v.fadeTick = 0

def fadeOutLMC():

    fadeout = pygame.Surface((640, 512))
    fadeout = fadeout.convert()
    if (v.fadeTick < 1):
        fadeout.fill((0,0,0))
    elif (v.fadeTick > 0 and v.fadeTick < 255): 
        fadeout.set_alpha(v.fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
    elif (v.fadeTick >= 256):
        fadeout.set_alpha(v.fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
        v.stateActual = v.STATE_ACE_FADE_IN
        v.fadeTick = 0

def fadeInACE():
    
    fadein = pygame.Surface((640, 512))
    fadein = fadein.convert()
    if (v.fadeTick < 1):
        fadein.fill((0,0,0))
    
    elif (v.fadeTick > 0 and v.fadeTick < 255): 
        fadein.set_alpha(255 - v.fadeTick)
        screen.blit(ACE, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
    elif (v.fadeTick >= 256):
        fadein.set_alpha(v.fadeTick)
        screen.blit(ACE,(0,0))
        screen.blit(fadein, (0,0))
        pygame.display.update()
        v.stateActual = v.STATE_ACE_FADE_OUT
        v.fadeTick = 0
        
def fadeOutACE():

    fadeout = pygame.Surface((640, 512))
    fadeout = fadeout.convert()
    if (v.fadeTick < 1):
        fadeout.fill((0,0,0))
    elif (v.fadeTick > 0 and v.fadeTick < 255):
        fadeout.set_alpha(v.fadeTick)
        screen.blit(ACE, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
    elif (v.fadeTick >= 256):
        fadeout.set_alpha(v.fadeTick)
        screen.blit(ACE, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
        v.stateActual = v.STATE_CREDITS_TEXT
        v.fadeTick = 0

def creditsDisplay():
    
    screen.fill((0, 85,85))
    for i in txt.message:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,v.creditsPosition))
        pygame.display.flip()
        v.creditsPosition += 16
        time.sleep(0.01)




