import pygame, sys, os, time,subprocess
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
        
fpsClock.tick(FPS)