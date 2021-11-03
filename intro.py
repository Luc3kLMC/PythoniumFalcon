import pygame, sys, os, time
import introMessageTxt as txt
import variables as v

pygame.init()


screen = pygame.display.set_mode((640,512))
font = pygame.font.Font("data\\Topaz-8.ttf", 16)



def page1Display():
    
    screen.fill((0, 85,85))
    for i in txt.page1:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,v.introPosition))
        pygame.display.flip()
        v.introPosition += 16
        time.sleep(0.1)

def page2Display():
    v.introPageControl += 1
    
    screen.fill((0, 85,85))
    for i in txt.page2:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,v.introPosition))
        pygame.display.flip()
        v.introPosition += 16
        time.sleep(0.1)







    






