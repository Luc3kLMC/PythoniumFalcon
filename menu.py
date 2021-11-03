import pygame, sys, os, time

from pygame import display
import variables as v
import credits
import intro


pygame.init()
screen = pygame.display.set_mode((640,512))
run = True
FPS = 100
fpsClock = pygame.time.Clock()

MENU = pygame.image.load(os.path.join("data", "title.png")).convert()

screen.blit(MENU, (0,0))
pygame.display.flip()

while run == True:
    if v.generalState == v.STATE_MENU:
        if v.menuBlit == 1:
            screen.blit(MENU, (0,0))
            pygame.display.flip()
            v.menuBlit = 0

        
        for event in pygame.event.get():
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    v.gameStartProc = True
                    exec(open('d8.py').read())
                elif event.key == pygame.K_c:
                    v.generalState = v.STATE_CREDITS
                    v.fadeTick = 0
                    v.stateActual = v.STATE_LMC_FADE_IN
                    #credits.Run()
                    #exec(open('credits.py').read())
                elif event.key == pygame.K_i:
                    v.generalState = v.STATE_INTRO
                elif event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_w and v.firstCheatEnabledWhenEqual3 == 0:
                    v.firstCheatEnabledWhenEqual3 += 1 
                elif event.key == pygame.K_t and v.firstCheatEnabledWhenEqual3 == 1:
                    v.firstCheatEnabledWhenEqual3 += 1
                elif event.key == pygame.K_f and v.firstCheatEnabledWhenEqual3 == 2:
                    v.firstCheatEnabledWhenEqual3 += 1  
                elif event.key == pygame.K_l and v.secondCheatEnabledWhenEqual3 == 0:
                    v.secondCheatEnabledWhenEqual3 += 1
                elif event.key == pygame.K_s and v.secondCheatEnabledWhenEqual3 == 1:
                    v.secondCheatEnabledWhenEqual3 += 1  
                elif event.key == pygame.K_a and v.secondCheatEnabledWhenEqual3 == 2:
                    v.secondCheatEnabledWhenEqual3 += 1
                elif event.key == pygame.K_v and v.thirdCheatEnabledWhenEqual3 == 0:
                    v.thirdCheatEnabledWhenEqual3 += 1
                elif event.key == pygame.K_p and v.thirdCheatEnabledWhenEqual3 == 1:
                    v.thirdCheatEnabledWhenEqual3 += 1
                elif event.key == pygame.K_r and v.thirdCheatEnabledWhenEqual3 == 2:
                    v.thirdCheatEnabledWhenEqual3 += 1        
        if event.type == pygame.QUIT:
                run = False
            
    if v.generalState == v.STATE_CREDITS:
        # written this way because i want to be able to skip all the fades 
        # with pressing Enter at any moment

        if (v.stateActual == v.STATE_LMC_FADE_IN):
            credits.fadeInLMC()
        elif (v.stateActual == v.STATE_LMC_FADE_OUT):
            credits.fadeOutLMC()
        elif (v.stateActual == v.STATE_ACE_FADE_IN):
            credits.fadeInACE()
        elif (v.stateActual == v.STATE_ACE_FADE_OUT):
            credits.fadeOutACE()
        elif (v.stateActual == v.STATE_CREDITS_TEXT and v.creditsDisplayed == 0):
            v.creditsDisplayed = 1
            credits.creditsDisplay()   

        if (v.stateActual != v.STATE_CREDITS_TEXT):
            v.fadeTick = v.fadeTick + 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    v.generalState = v.STATE_MENU
                    v.menuBlit = 1

                elif event.key == pygame.K_ESCAPE:
                    run = False

    if v.generalState == v.STATE_INTRO:
        if v.introPageControl == 0:
            intro.page1Display()
            v.introPageControl += 1
            v.introPosition = 0
        elif v.introPageControl == 2:
            intro.page2Display()
            v.introPageControl += 1
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and v.introPageControl == 4:
                    v.introPageControl = 0
                    v.introPosition = 0
                    v.generalState = v.STATE_MENU
                    v.menuBlit = 1
                    #execfile('menu.py')

                elif event.key == pygame.K_RETURN and v.introPageControl == 1:
                    v.introPageControl += 1
                
                elif event.key == pygame.K_ESCAPE:
                    run = False

        
    fpsClock.tick(FPS)
