import pygame, sys, os, time

from pygame import display
import variables as v
import credits
import intro
import d8
import arraysLevels as arrays
import robboTxt


pygame.init()
screen = pygame.display.set_mode((640,512))
run = True
FPS = 200
fpsClock = pygame.time.Clock()

MENU = pygame.image.load(os.path.join("data", "title.png")).convert()

##### disable mouse 
pygame.event.set_blocked(pygame.MOUSEMOTION)

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
                    d8.bg = pygame.image.load(os.path.join("data\\background", "bg1.png")).convert() # background image nr 1
                    screen.blit(d8.bg, (0,0))
                    d8.displayOnHUD()
                    d8.drawTiles()
                    v.gameStartProc = True
                    v.generalState = v.STATE_GAME
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

    if v.generalState == v.STATE_GAME:
        pygame.display.flip()

        # handling with idle animations:
        v.portalGlowTick += 1
        if (v.portalGlowTick > v.PORTAL_TICK_TEMPO):
            v.portalGlowFrame += 1
            d8.portalGlowAnim()
            v.portalGlowTick = 0
            if (v.portalGlowFrame == 7):
                v.portalGlowFrame = 0
        
        v.redCapacitorAnimTick += 1
        if (v.redCapacitorAnimTick > v.CAPACITOR_TICK_TEMPO):
            v.redCapacitorAnimTick = 0
        
        v.blueCapacitorAnimTick += 1
        if (v.blueCapacitorAnimTick > v.CAPACITOR_TICK_TEMPO):
            v.blueCapacitorAnimTick = 0

        if v.falconIdleControl == 1:
            v.falconIdle += 1

        if v.flyingAnimControl == 1:
            v.flyingTick += 1

        #if v.flyingAnimControl == 2:
        #    falconFlying()
        #    v.flyingAnimControl = 0
        
        d8.falconHittingStone()
        d8.redCapacitorsAnim()
        d8.blueCapacitorsAnim()

        d8.robboScrollUp()
        d8.robboSays()
        d8.robboScrollDown()

        if v.flyingAnimControl == 3:
            v.flyingAnimControl = 4

        d8.falconFlying()
        d8.falconIdleAnimation()

        if v.levelScoreControl != v.LEVEL_SCORE_OFF:
            v.levelScoreTick += 1
            d8.levelScore()

        if v.flyingAnimControl == 4:
            v.flyingAnimControl = 1

        if v.hudScrollingControl == v.ON:
            v.hudScrollingTick += 4 # This is the tempo of robboHUD scrolling up and down

        if v.stoneHitAnimControl == 1:
            v.stoneHitAnimTick += 1

        v.kierunek = 0

        if (v.coal == 0 and v.levelScoreControl != v.LEVEL_SCORE_NOCOAL):
            v.levelScoreControl = v.LEVEL_SCORE_NOCOAL

        

        


        if v.gameStartProc == True:
            screen.blit(d8.bg, (0,0))
            d8.displayOnHUD()
            d8.kamyki = arrays.dict_levels[1]
            d8.drawTiles()
            v.gameStartProc = False

        
        

        if v.endLevelCheck == True:
            v.endLevelCheck = False
            d8.nextLevel()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    v.kierunek = 1
                    v.falconFace = 0
                elif event.key == pygame.K_LEFT:
                    v.kierunek = 2
                    v.falconFace = 64
                elif event.key == pygame.K_UP:
                    v.kierunek = 3
                elif event.key == pygame.K_DOWN:
                    v.kierunek = 4 
                elif event.key == pygame.K_n and v.firstCheatEnabledWhenEqual3 == 3:
                    v.level += 1
                    d8.nextLevel()   
                    

                elif event.key == pygame.K_ESCAPE:
                    d8.clearTiles()
                    d8.clean()
                    v.generalState = v.STATE_MENU
                    v.menuBlit = 1
                
                #falconWholeFrameMovePrep()

            

        if v.kierunek != 0:
            if v.robboMsgCtrl == v.SCROLL_DOWN:
                v.hudScrollingControl = v.ON
                v.hudScrollingTick = 0

            if v.flyingAnimControl == 0:
                v.kierunekHold = v.kierunek
                d8.isThisStone()
                d8.czyRamka()
                d8.falconCollisionCheck()

        #if v.robboMsgCtrl == v.SCROLL_DISPLAY:
        #    robboSays()

        if v.youWin == 1:
            v.youWin = 0
            exec(open("score.py").read())
        if v.youWin == 2:
            v.youWin = 0
            exec(open("gameover.py").read())
        if v.youWin == 3:
            v.youWin = 0
            exec(open("leakedGameOver.py").read())

        
    fpsClock.tick(FPS)
