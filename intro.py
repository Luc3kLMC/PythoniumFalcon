import pygame, sys, os, time
import introMessageTxt as txt

pygame.init()

run = True
screen = pygame.display.set_mode((640,512))
font = pygame.font.Font("data\\Topaz-8.ttf", 16)
position = 0
pageControl = 0


def page1Display():
    global position
    global pageControl
    pageControl += 1
    screen.fill((0, 85,85))
    for i in txt.page1:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,position))
        pygame.display.flip()
        position += 16
        time.sleep(0.1)

def page2Display():
    global position
    global pageControl
    pageControl += 1
    position = 0
    screen.fill((0, 85,85))
    for i in txt.page2:
        blitTxt = font.render(str(i), True, (0,153,153))
        screen.blit(blitTxt, (0,position))
        pygame.display.flip()
        position += 16
        time.sleep(0.1)




page1Display()
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and pageControl == 1:
                page2Display()
            elif event.key == pygame.K_RETURN and pageControl == 2:
                execfile('menu.py')
            elif event.key == pygame.K_ESCAPE:
                run = False






