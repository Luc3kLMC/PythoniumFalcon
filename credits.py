
import pygame, sys, os, time
import creditsTxt as txt 

pygame.init()
screen = pygame.display.set_mode((640,512))
run = True
FPS = 100
fpsClock = pygame.time.Clock()

# kinda enum style 
STATE_LMC_FADE_IN = 1
STATE_LMC_FADE_OUT = 2
STATE_ACE_FADE_IN = 3
STATE_ACE_FADE_OUT = 4
STATE_CREDITS_TEXT= 5

fadeTick = 0
stateActual = STATE_LMC_FADE_IN  # controling the phase we're already in
creditsDisplayed = 0

LMC = pygame.image.load(os.path.join("data", "LMC.png")).convert()
ACE = pygame.image.load(os.path.join("data", "ACE.png")).convert()

font = pygame.font.Font("data\\Topaz-8.ttf", 16)
position = 0

def fadeInLMC():
    global fadeTick,stateActual
    fadein = pygame.Surface((640, 512))
    fadein = fadein.convert()
    if (fadeTick < 1):
        fadein.fill((0,0,0))
    elif (fadeTick > 0 and fadeTick < 255): 
        fadein.set_alpha(255 - fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
    elif (fadeTick >= 256):
        fadein.set_alpha(fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
        stateActual = STATE_LMC_FADE_OUT
        fadeTick = 0

def fadeOutLMC():
    global fadeTick,stateActual
    fadeout = pygame.Surface((640, 512))
    fadeout = fadeout.convert()
    if (fadeTick < 1):
        fadeout.fill((0,0,0))
    elif (fadeTick > 0 and fadeTick < 255): 
        fadeout.set_alpha(fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
    elif (fadeTick >= 256):
        fadeout.set_alpha(fadeTick)
        screen.blit(LMC, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
        stateActual = STATE_ACE_FADE_IN
        fadeTick = 0
 
def fadeInACE():
    global fadeTick, stateActual
    fadein = pygame.Surface((640, 512))
    fadein = fadein.convert()
    if (fadeTick < 1):
        fadein.fill((0,0,0))
    
    elif (fadeTick > 0 and fadeTick < 255): 
        fadein.set_alpha(255 - fadeTick)
        screen.blit(ACE, (0,0))
        screen.blit(fadein, (0, 0))
        pygame.display.update()
    elif (fadeTick >= 256):
        fadein.set_alpha(fadeTick)
        screen.blit(ACE,(0,0))
        screen.blit(fadein, (0,0))
        pygame.display.update()
        stateActual = STATE_ACE_FADE_OUT
        fadeTick = 0
        
def fadeOutACE():
    global fadeTick,stateActual
    fadeout = pygame.Surface((640, 512))
    fadeout = fadeout.convert()
    if (fadeTick < 1):
        fadeout.fill((0,0,0))
    elif (fadeTick > 0 and fadeTick < 255):
        fadeout.set_alpha(fadeTick)
        screen.blit(ACE, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
    elif (fadeTick >= 256):
        fadeout.set_alpha(fadeTick)
        screen.blit(ACE, (0,0))
        screen.blit(fadeout, (0, 0))
        pygame.display.update()
        stateActual = STATE_CREDITS_TEXT
        fadeTick = 0

def creditsDisplay():
    global position
    screen.fill((0, 85,85))
    for i in txt.message:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,position))
        pygame.display.flip()
        position += 16
        time.sleep(0.01)

while run:
    # written this way because i want to be able to skip all the fades 
    # with pressing Enter at any moment

    if (stateActual == STATE_LMC_FADE_IN):
        fadeInLMC()
    elif (stateActual == STATE_LMC_FADE_OUT):
        fadeOutLMC()
    elif (stateActual == STATE_ACE_FADE_IN):
        fadeInACE()
    elif (stateActual == STATE_ACE_FADE_OUT):
        fadeOutACE()
    elif (stateActual == STATE_CREDITS_TEXT and creditsDisplayed == 0):
        creditsDisplayed = 1
        creditsDisplay()   

    if (stateActual != STATE_CREDITS_TEXT):
        fadeTick = fadeTick + 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                exec(open('menu.py').read())
            elif event.key == pygame.K_ESCAPE:
                run = False
    
    fpsClock.tick(FPS)


