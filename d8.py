import pygame, sys, os, random
import arrays
import variables as v

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()  # needed for 'wait vbl'
random.seed(567) # stone-tile randomizer seed
stoneTileRandom = random.randint(1, 3)


screen = pygame.display.set_mode((640,512))
pygame.display.set_caption("AtareniumPython")
run = True
font = pygame.font.SysFont("Topaz-8", 16)

bg = pygame.image.load(os.path.join("data", "tlo1.png")).convert() # background image nr 1
HUD = pygame.image.load(os.path.join("data", "HUD.png")).convert()

coalDisplay = font.render(str(v.coal), True, (0,153,153))

kamyki = arrays.level1


idleFrame = 0  # variable controlling the idle animation time

    # atarenium falcon idle graphics
    # pointing right
falconR1 = pygame.image.load(os.path.join("data", "falconR1.png"))
falconR1.set_colorkey((0,0,0))
    # other gfx
coal2 = pygame.image.load(os.path.join("data", "Coal2.png"))
coal2.set_colorkey((0,0,0))
coal3 = pygame.image.load(os.path.join("data", "Coal3.png"))
coal3.set_colorkey((0,0,0))
coal4 = pygame.image.load(os.path.join("data", "Coal4.png"))
coal4.set_colorkey((0,0,0))
coal5 = pygame.image.load(os.path.join("data", "Coal5.png"))
coal5.set_colorkey((0,0,0))
blueCapacitor = pygame.image.load(os.path.join("data", "BlueCapacitor0.png"))
blueCapacitor.set_colorkey((0,0,0))
redCapacitor = pygame.image.load(os.path.join("data", "RedCapacitor0.png"))
redCapacitor.set_colorkey((0,0,0))
portal = pygame.image.load(os.path.join("data", "AtariPortal.png"))
portal.set_colorkey((0,0,0))
robbo = pygame.image.load(os.path.join("data", "Robbo.png"))
robbo.set_colorkey((0,0,0))


#### FUNCTIONS

def falconWholeFrameMovePrep():
    v.falconPreviousPositionX = v.falconPositionX
    v.falconPreviousPositionY = v.falconPositionY

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
    stoneCollisionCheck()
    falconWholeFrameMoveBlit()


def drawTiles():
    for i in range(len(kamyki)):
        for j in range(len(kamyki[i])): 
            if kamyki[i][j] == 1:
                v.falconPositionX = i
                v.falconPositionY = j
                screen.blit(falconR1, (v.falconPositionX,v.falconPositionY))
            
            if kamyki[i][j] == 3:
                stoneTileRandom = random.randint(1, 3)
                stone1 = pygame.image.load(os.path.join("data", "stone"+ str(stoneTileRandom) +".png"))
                stone1.set_colorkey((0,0,0))
                screen.blit(stone1, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 4:
                screen.blit(coal2, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 5:
                screen.blit(coal3, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 6:                
                screen.blit(coal4, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 7:               
                screen.blit(coal5, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 8:               
                screen.blit(blueCapacitor, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 9:                
                screen.blit(redCapacitor, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 10:               
                screen.blit(portal, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            if kamyki[i][j] == 11:               
                screen.blit(robbo, (i * v.TILE_SIZE, j * v.TILE_SIZE))
            

    

    

def falconWholeFrameMoveBlit():
    screen.blit(bg, (v.falconPreviousPositionX * v.TILE_SIZE, v.falconPreviousPositionY * v.TILE_SIZE), pygame.Rect((v.falconPreviousPositionX * v.TILE_SIZE, v.falconPreviousPositionY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
    screen.blit(falconR1, (v.falconPositionX * v.TILE_SIZE,v.falconPositionY * v.TILE_SIZE))   
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

def stoneCollisionCheck():
    for i in range(len(kamyki)):
        for j in range(len(kamyki[i])): 
            if kamyki[v.falconPositionX][v.falconPositionY] == 3:
                v.falconPositionX = v.falconPreviousPositionX
                v.falconPositionY = v.falconPreviousPositionY
                
        
        


##### disable mouse 
pygame.event.set_blocked(pygame.MOUSEMOTION)

##### screen display after preparing everything
screen.blit(bg, (0,0))
screen.blit(HUD, (0,448))
screen.blit(coalDisplay, (84,464))   

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





    

