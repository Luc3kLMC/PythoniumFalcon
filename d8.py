import pygame, sys, os
import arrays
import variables as v

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()  # needed for 'wait vbl'
screen = pygame.display.set_mode((640,512))
pygame.display.set_caption("AtareniumPython")
run = True
font = pygame.font.SysFont("topaz", 16)

bg = pygame.image.load(os.path.join("data", "tlo1.png")).convert() # background image nr 1


arrayPos = arrays.kamyki[1][0]    #  Y,X  !!!! 




# arrayCheck = font.render(str (arrayPos), True, (55,5,75))

idleFrame = 0  # variable controlling the idle animation time

    # atarenium falcon idle graphics
    # pointing right
falconR1 = pygame.image.load(os.path.join("data", "falconR1.png"))
falconR1.set_colorkey((0,0,0))



#### FUNCTIONS

def falconWholeFrameMovePrep():
    if v.movementDirection == 1:
        v.falconPositionX += 1
    elif v.movementDirection == 2:
        v.falconPositionX -= 1
    elif v.movementDirection == 3:
        v.falconPositionY -= 1
    elif v.movementDirection == 4:
        v.falconPositionY += 1
   
    v.movementDirection = 0
    falconWholeFrameMoveBlit()

    

def falconWholeFrameMoveBlit():
    screen.blit(bg, (0,0))
    screen.blit(falconR1, (v.falconPositionX * 64,v.falconPositionY * 64))   
    pygame.display.flip()
        
        


##### disable mouse 
pygame.event.set_blocked(pygame.MOUSEMOTION)

##### screen display after preparing everything
screen.blit(bg, (0,0))
screen.blit(falconR1, (v.falconPositionX,v.falconPositionY))
pygame.display.flip()

##### MAIN LOOP
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                v.movementDirection = 1
            elif event.key == pygame.K_LEFT:
                v.movementDirection = 2
            elif event.key == pygame.K_UP:
                v.movementDirection = 3
            elif event.key == pygame.K_DOWN:
                v.movementDirection = 4 
             
        
        falconWholeFrameMovePrep()

    
    fpsClock.tick(FPS)    # wait vbl





    

