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


arrayPos = arrays.kamyki[9][6]    #  Y,X  !!!! 




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
    frameCollisionCheck()
    falconWholeFrameMoveBlit()


def drawTiles():
    for i in range(len(arrays.kamyki)):
        for j in range(len(arrays.kamyki[i])): 
            if arrays.kamyki[i][j] == 1:
                stone1 = pygame.image.load(os.path.join("data", "stone1.png"))
                screen.blit(stone1, (i * 64, j * 64))
    

    

def falconWholeFrameMoveBlit():
    screen.blit(bg, (0,0))
    screen.blit(falconR1, (v.falconPositionX * 64,v.falconPositionY * 64))   
    pygame.display.flip()

def frameCollisionCheck():
    if v.falconPositionX == v.MAP_TILE_WIDTH + 1:    # RIGHT BORDER
        v.falconPositionX = v.MAP_TILE_WIDTH
    elif v.falconPositionX == -1:                   # LEFT BORDER
        v.falconPositionX = 0
    elif v.falconPositionY == v.MAP_TILE_HEIGHT + 1:  # DOWN BORDER
        v.falconPositionY = v.MAP_TILE_HEIGHT
    elif v.falconPositionY == -1:                      # UP BORDER
        v.falconPositionY = 0
        
        


##### disable mouse 
pygame.event.set_blocked(pygame.MOUSEMOTION)

##### screen display after preparing everything
screen.blit(bg, (0,0))
screen.blit(falconR1, (v.falconPositionX,v.falconPositionY))
drawTiles()
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





    

