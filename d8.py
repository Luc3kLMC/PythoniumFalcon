import pygame, sys, os, random, time
import arraysLevels as arrays
import variables as v  
import robboTxt 

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()  # needed for 'wait vbl'
random.seed(567) # stone-tile randomizer seed
stoneTileRandom = random.randint(1, 3)

screen = pygame.display.set_mode((640,512))
pygame.display.set_caption("PythoniumFalcon")
run = True
font = pygame.font.Font("data\\Topaz-8.ttf", 16)
#font = pygame.font.Font(os.path.join("data", "Topaz-8.ttf"), 16)

tileset = pygame.image.load(os.path.join("data","tileset.png")).convert()
tileset.set_colorkey((0,0,0))

bg = pygame.image.load(os.path.join("data\\background", "bg1.png")).convert() # background image nr 1
HUD = pygame.image.load(os.path.join("data", "HUD.png")).convert() # HUD image
robboHUD = pygame.image.load(os.path.join("data", "falkon_robbo.png")).convert()
gameOver = pygame.image.load(os.path.join("data", "gej_ower.png")).convert()

coalDisplay = font.render(str(v.coal), True, (0,153,153))  # variable to display current coal amount on HUD
excessCoalDisplay = font.render(str(v.excessCoal), True, (0,153,153)) # ... amount of extra coal for endgame score
capacitorsDisplay = font.render(str(v.capacitors), True, (0,153,153)) # ... capacitors for endgame score
robboDisplay = font.render(str(v.robboMsgCount), True, (0,153,153)) # same for Robbo's

kamyki = arrays.dict_levels[v.level]
robboMessages = robboTxt.dict_robboTxt[v.robboMsgNr]


idleFrame = 0  # variable controlling the idle animation time

    # atarenium falcon idle graphics  UNUSED - BADLY HANDLED, FULL TILESET IMPLEMENTED !
    # pointing right
#falconR1 = pygame.image.load(os.path.join("data\\tilesFalcon", "falconR1.png"))
#falconR1.set_colorkey((0,0,0))
    # other gfx
#coal2 = pygame.image.load(os.path.join("data\\tilesCoal", "Coal2.png"))
#coal2.set_colorkey((0,0,0))
#coal3 = pygame.image.load(os.path.join("data\\tilesCoal", "Coal3.png"))
#coal3.set_colorkey((0,0,0))
#coal4 = pygame.image.load(os.path.join("data\\tilesCoal", "Coal4.png"))
#coal4.set_colorkey((0,0,0))
#coal5 = pygame.image.load(os.path.join("data\\tilesCoal", "Coal5.png"))
#coal5.set_colorkey((0,0,0))
#blueCapacitor = pygame.image.load(os.path.join("data", "BlueCapacitor0.png"))
#blueCapacitor.set_colorkey((0,0,0))
#redCapacitor = pygame.image.load(os.path.join("data", "RedCapacitor0.png"))
#redCapacitor.set_colorkey((0,0,0))
#portal = pygame.image.load(os.path.join("data", "AtariPortal.png"))
#portal.set_colorkey((0,0,0))
#robbo = pygame.image.load(os.path.join("data", "Robbo.png"))
#robbo.set_colorkey((0,0,0))


#### FUNCTIONS

def clean():
    #TBD
    return

def endLevelFadeOut():
    #TBD  
    return  


def falconWholeFrameMovePrep():
    v.falconPreviousPositionX = v.falconX
    v.falconPreviousPositionY = v.falconY

    if v.kierunek == 1:
        v.falconX += 1
    elif v.kierunek == 2:
        v.falconX -= 1
    elif v.kierunek == 3:
        v.falconY -= 1
    elif v.kierunek == 4:
        v.falconY += 1

    
        

    v.kierunek = 0
    
    falconCollisionCheck()
    isThisStone()
    falconWholeFrameMoveBlit()
    coalAndCollect()
    
    displayOnHUD()
    gameOverCheck()
    if v.robboMsgCtrl == v.SCROLL_DISPLAY:
        v.robboMsgCtrl = v.SCROLL_DOWN
        v.hudScrollingControl = v.ON   
    
def clearTiles():
    global kamyki
    for i in range(len(kamyki)):
        for j in range(len(kamyki[i])):
            kamyki[i][j] = 0
            v.collectiblesAnim[i][j] = 0
            
def drawTiles():
    global kamyki
    kamyki = arrays.dict_levels[v.level]
    for i in range(len(kamyki)):
        for j in range(len(kamyki[i])): 
            if kamyki[i][j] == 1:
                v.falconX = i
                v.falconY = j
                v.krawedzX = i
                v.krawedzY = j
                v.uwPosX = v.falconX * 64
                v.uwPosY = v.falconY * 64
                v.tempX = v.falconX
                v.tempY = v.falconY
                screen.blit(tileset, (v.falconX * v.TILE_SIZE,v.falconY * v.TILE_SIZE),(0,128,64,64))
            
            if kamyki[i][j] == 3:
                stoneTileRandom = random.randint(0, 2)
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(stoneTileRandom * 64,0,64,64))
            if kamyki[i][j] == 4:
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(3 * 64,0,64,64))
            if kamyki[i][j] == 5:
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(4*64,0,64,64))
            if kamyki[i][j] == 6:                
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(5*64,0,64,64))
            if kamyki[i][j] == 7:               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(6*64,0,64,64))
            if kamyki[i][j] == 8:
                v.collectiblesAnim[i][j] = 8               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(0,64,64,64))
            if kamyki[i][j] == 9: 
                v.collectiblesAnim[i][j] = 9               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(64,64,64,64))
            if kamyki[i][j] == 10:
                v.portalGlowX = i
                v.portalGlowY = j               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(128,64,64,64))
            if kamyki[i][j] == 11:               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(192,64,64,64))
            if kamyki[i][j] == 12:
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(256,64,64,64))
    
def displayOnHUD():
    if v.robboMsgCtrl != v.SCROLL_OFF:
        return
    if v.amigaMode != v.AMIGA_MODE_OFF:
        return


    coalDisplay = font.render(str(v.coal), True, (0,153,153))  
    excessCoalDisplay = font.render(str(v.excessCoal), True, (0,153,153)) 
    capacitorsDisplay = font.render(str(v.capacitors), True, (0,153,153)) 
    robboDisplay = font.render(str(v.robboMsgCount), True, (0,153,153))
    screen.blit(HUD, (0,448))
    screen.blit(coalDisplay, (84,464))
    screen.blit(excessCoalDisplay, (260,464))
    screen.blit(capacitorsDisplay, (380,472))
    screen.blit(robboDisplay, (500,472)) 
    #pygame.display.flip()   
    
def coalAndCollect():
    

    pickSthX = v.falconX
    pickSthY = v.falconY

    whatPicked = kamyki[pickSthX][pickSthY]
    kamyki[pickSthX][pickSthY] = 0
    v.collectiblesAnim[pickSthX][pickSthY] = 0

    if v.secondCheatEnabledWhenEqual3 == 3:
        v.coal += 1

    v.coal -= 1

    if whatPicked == 4:
        v.coal += 2
    elif whatPicked == 5:
        v.coal += 3
    elif whatPicked == 6:
        v.coal +=4
    elif whatPicked == 7:
        v.coal += 5
    elif whatPicked == 8:
        v.capacitors += 2
    elif whatPicked == 9:
        v.capacitors += 4
    elif whatPicked == 10:  # portal ending level
        v.levelScoreControl = v.LEVEL_SCORE_COUNT
        v.falconIdleControl = 1
    elif whatPicked == 11:
        v.robboMsgNr += 1
        v.robboMsgCount += 1
        v.robboMsgCtrl = v.SCROLL_UP
        v.hudScrollingControl = v.ON
    elif whatPicked == 12:
        if v.thirdCheatEnabledWhenEqual3 == 3:
            v.youWin = 3
            return
        if v.thirdCheatEnabledWhenEqual3 != 3:
            v.amigaMode = v.AMIGA_MODE_ON # used once to switch mode
            if v.amigaMode == v.AMIGA_MODE_ON: 
                v.amigaMode = v.AMIGA_MODE_CHECK # and now set to check ending
                # AMIGA MODE TBD

def falconHittingStone():
    if v.stoneHitAnimControl != 1:
        return
    
    posX = v.falconX * 64
    posY = v.falconY * 64

    if v.stoneHitAnimControl == 1:
        if v.stoneHitAnimTick == v.falconIdleTempo * 1:
            v.stoneHitAnimFrame = 0
            if (v.oneFrameDirection == 1):
                posX += 1
            elif (v.oneFrameDirection == 2):
                posX -= 1
            elif (v.oneFrameDirection == 3):
                posY -= 1
            elif (v.oneFrameDirection == 4):
                posY += 1
        elif v.stoneHitAnimTick == v.falconIdleTempo * 2:
            v.stoneHitAnimFrame = 1
        elif v.stoneHitAnimTick == v.falconIdleTempo * 3:
            v.stoneHitAnimFrame = 2
            if (v.oneFrameDirection == 1):
                posX += 1
            elif (v.oneFrameDirection == 2):
                posX -= 1
            elif (v.oneFrameDirection == 3):
                posY -= 1
            elif (v.oneFrameDirection == 4):
                posY += 1
        elif v.stoneHitAnimTick == v.falconIdleTempo * 4:
            v.stoneHitAnimFrame = 3
        elif v.stoneHitAnimTick == v.falconIdleTempo * 5:
            v.stoneHitAnimFrame = 4
            if (v.oneFrameDirection == 1):
                posX += 1
            elif (v.oneFrameDirection == 2):
                posX -= 1
            elif (v.oneFrameDirection == 3):
                posY -= 1
            elif (v.oneFrameDirection == 4):
                posY += 1
        elif v.stoneHitAnimTick == v.falconIdleTempo * 6:
            v.stoneHitAnimFrame = 5
        elif v.stoneHitAnimTick == v.falconIdleTempo * 7:
            v.stoneHitAnimFrame = 6
            if (v.oneFrameDirection == 1):
                posX += 1
            elif (v.oneFrameDirection == 2):
                posX -= 1
            elif (v.oneFrameDirection == 3):
                posY -= 1
            elif (v.oneFrameDirection == 4):
                posY += 1
        elif v.stoneHitAnimTick == v.falconIdleTempo * 8:
            v.stoneHitAnimFrame = 7
            v.stoneHitAnimTick = 0
            v.stoneHitAnimControl = 0
            v.falconIdleControl = 1

    screen.blit(bg, (posX * v.TILE_SIZE, posY * v.TILE_SIZE), pygame.Rect((posX * v.TILE_SIZE, posY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
    screen.blit(tileset, (v.falconX * v.TILE_SIZE,v.falconY * v.TILE_SIZE),(v.stoneHitAnimFrame * 64,v.falconFace + 128,64,64))   



def levelScore():
    if (v.levelScoreControl == v.LEVEL_SCORE_OFF):
        return
    if (v.coal == 1 and v.levelScoreControl == v.LEVEL_SCORE_COUNT):
        v.levelScoreControl = v.LEVEL_SCORE_PORTAL_OPEN
        v.falconIdleControl = False
    if (v.amigaMode == v.AMIGA_MODE_OFF and v.levelScoreTick == v.levelScoreTempo and v.levelScoreControl == v.LEVEL_SCORE_COUNT):
        v.levelScoreTick = 0
        v.coal -= 1
        v.excessCoal += 1
        displayOnHUD()
    if (v.amigaMode != v.AMIGA_MODE_OFF and v.levelScoreTick == v.levelScoreTempo and v.levelScoreControl == v.LEVEL_SCORE_COUNT):
        v.levelScoreTick = 0
        v.coal -= 1
        v.excessCoal += 1
        # TBD GOTEK ANIMATED !!!
    if (v.levelScoreTick == v.PORTAL_TICK_TEMPO and v.levelScoreControl == v.LEVEL_SCORE_PORTAL_OPEN):
        v.levelScoreTick = 0
        screen.blit(bg, (v.falconX * v.TILE_SIZE, v.falconY * v.TILE_SIZE), pygame.Rect((v.falconX * v.TILE_SIZE, v.falconY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
        screen.blit(tileset, (v.falconX * v.TILE_SIZE,v.falconY * v.TILE_SIZE),(v.levelAnimFrame*64,10*64,64,64))
        screen.blit(tileset, (v.falconX*64,v.falconY*64),(v.levelAnimFrame*64,v.falconFace+(6*64),64,64))
        v.levelAnimFrame += 1
        if v.levelAnimFrame == 8:
            v.levelAnimFrame = 0
            v.levelScoreControl = v.LEVEL_SCORE_PORTAL_ANIM

    if (v.levelScoreTick == v.PORTAL_TICK_TEMPO and v.levelScoreControl == v. LEVEL_SCORE_PORTAL_ANIM):
        v.levelScoreTick = 0
        screen.blit(bg, (v.falconX * v.TILE_SIZE, v.falconY * v.TILE_SIZE), pygame.Rect((v.falconX * v.TILE_SIZE, v.falconY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
        screen.blit(tileset, (v.falconX*64,v.falconY*64),(v.levelAnimFrame*64,v.falconFace+(4*64),64,64))
        v.levelAnimFrame += 1
        if v.levelAnimFrame == 8:
            v.levelAnimFrame = 0
            v.levelScoreControl = v.LEVEL_SCORE_PORTAL_CLOSE
    
    if (v.levelScoreTick == v.PORTAL_TICK_TEMPO and v.levelScoreControl == v. LEVEL_SCORE_PORTAL_CLOSE):
        v.levelScoreTick = 0
        screen.blit(bg, (v.falconX * v.TILE_SIZE, v.falconY * v.TILE_SIZE), pygame.Rect((v.falconX * v.TILE_SIZE, v.falconY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
        screen.blit(tileset, (v.falconX*64,v.falconY*64),(448 - (v.levelAnimFrame*64),(10*64),64,64))
        v.levelAnimFrame += 1
        if v.levelAnimFrame == 8:
            v.levelAnimFrame = 0
            v.levelScoreControl = v.LEVEL_SCORE_END    

    
    if (v.amigaMode == v.AMIGA_MODE_OFF and v.levelScoreTick == 64 and v.levelScoreControl == v.LEVEL_SCORE_NOCOAL):
        v.levelScoreTick = 0
        displayOnHUD()
        v.levelAnimFrame += 1
        if (v.levelAnimFrame == 2):
            v.youWin = 2
            v.HUDfontcolor = (0,153,153)
            v.levelAnimFrame = 0
            v.levelScoreControl = v.LEVEL_SCORE_OFF
            clean()
    # AMIGA MODE NOT SURE IF OK TBD
    if (v.amigaMode != v.AMIGA_MODE_OFF and v.levelScoreTick == 64 and v.levelScoreControl == v.LEVEL_SCORE_NOCOAL):
        v.levelScoreTick = 0
        displayOnHUD()
        v.levelAnimFrame += 1
        if (v.levelAnimFrame == 2):
            v.youWin = 2
            v.HUDfontcolor = (0,153,153)
            v.levelAnimFrame = 0
            v.levelScoreControl = v.LEVEL_SCORE_OFF
            clean()
    
    if (v.levelScoreControl == v.LEVEL_SCORE_END):
        v.levelScoreControl = v.LEVEL_SCORE_OFF
        endLevelFadeOut()
        v.falconIdleControl = True
        v.portalAnimTick = 0
        v.level += 1
        if (v.level == v.LAST_LEVEL_NUMBER + 1):
            v.youWin = 1
        else:
            nextLevel()
    
def gameOverCheck():
    if v.coal == 0:
                            # red '0' flicking to indicate game over - zero fuel
        for i in range(3):    
            coalDisplay = font.render(str(v.coal), True, (204,0,0))  
            screen.blit(HUD, (0,448))
            screen.blit(coalDisplay, (84,464))
            screen.blit(excessCoalDisplay, (260,464))
            screen.blit(capacitorsDisplay, (380,472))
            screen.blit(robboDisplay, (500,472)) 
            pygame.display.flip() 
            time.sleep(0.5)
            coalDisplay = font.render(str(v.coal), True, (0,153,153))
            screen.blit(HUD, (0,448))
            screen.blit(coalDisplay, (84,464))
            screen.blit(excessCoalDisplay, (260,464))
            screen.blit(capacitorsDisplay, (380,472))
            screen.blit(robboDisplay, (500,472)) 
            pygame.display.flip() 
            time.sleep(0.5)
            

        v.coal = v.startingCoal
        v.level = 1
        v.robboMsgCount = 0
        v.falconX = 0
        v.falconPreviousPositionY = 0
        exec(open("gameover.py").read())

def robboScrollUp():
    if v.robboMsgCtrl != v.SCROLL_UP:
        return

    if v.hudScrollingControl == v.ON: 
        screen.blit(robboHUD, (0,512 - v.hudScrollingTick)) 
    
    if v.hudScrollingTick >= 64:
        v.robboMsgCtrl = v.SCROLL_DISPLAY
        v.hudScrollingControl = 0
        v.hudScrollingTick = 0

def robboSays():
    if v.robboMsgCtrl != v.SCROLL_DISPLAY:
        return
    if v.amigaMode == v.AMIGA_MODE_CHECK:
        return # temporary, TBD        

    elif v.amigaMode != v.AMIGA_MODE_CHECK:
        global robboMessages 
        robboPreMsgDisplay = font.render("ROBBO says:", True, (0,153,153)) 
        robboMsgDisplay = font.render(str(robboMessages), True, (0,153,153)) 
        screen.blit(robboPreMsgDisplay, (16,460)) 
        screen.blit(robboMsgDisplay, (16,480)) 
        v.robboMsgNr +=1 
        robboMessages = robboTxt.dict_robboTxt[v.robboMsgNr] 
        v.robboMsgCtrl = v.SCROLL_DOWN
        v.hudScrollingTick = 0 

def robboScrollDown():
    if v.robboMsgCtrl != v.SCROLL_DOWN:
        return
    
    if v.hudScrollingControl == v.ON:
        screen.blit(HUD, (0,448))
        screen.blit(robboHUD, (0,448 + v.hudScrollingTick))
     
    if v.hudScrollingTick >= 64:     
        v.robboMsgCtrl = v.SCROLL_OFF
        v.hudScrollingTick = 0
        v.hudScrollingControl = 0
        displayOnHUD()
    
def falconWholeFrameMoveBlit():
    screen.blit(bg, (v.falconPreviousPositionX * v.TILE_SIZE, v.falconPreviousPositionY * v.TILE_SIZE), pygame.Rect((v.falconPreviousPositionX * v.TILE_SIZE, v.falconPreviousPositionY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
    screen.blit(tileset, (v.falconX * v.TILE_SIZE,v.falconY * v.TILE_SIZE),(0,128,64,64))   
    #pygame.display.flip()
    
def falconCollisionCheck():
    if v.stoneHit == 1:
        v.stoneHitAnimControl = 1
        v.falconIdleControl = 0
    
    if v.kierunek == 1:
        v.krawedzX -= 1
    if v.kierunek == 2:
        v.krawedzX += 1
    if v.kierunek == 3:
        v.krawedzY += 1
    if v.kierunek == 4:
        v.krawedzY -= 1

    v.stoneHit = 0
    
    if v.frameHit == 1:
        v.stoneHitAnimControl = 1
        v.falconIdleControl = 0
        v.frameHit = 0

    prepareFalconFlying()
    v.flyingAnimControl = 1 


    if v.falconX == v.MAP_TILE_WIDTH + 1:    # RIGHT BORDER
        v.falconX = v.MAP_TILE_WIDTH
        v.frameHit = 1
    elif v.falconX == -1:                   # LEFT BORDER
        v.falconX = 0
        v.frameHit = 1
    elif v.falconY == v.MAP_TILE_HEIGHT + 1:  # DOWN BORDER
        v.falconY = v.MAP_TILE_HEIGHT
        v.frameHit = 1
    elif v.falconY == -1:                      # UP BORDER
        v.falconY = 0
        v.frameHit = 1

def isThisStone():
    for i in range(len(kamyki)):
        for j in range(len(kamyki[i])): 
            if kamyki[v.falconX][v.falconY] == 3:
                v.falconX = v.falconPreviousPositionX
                v.falconY = v.falconPreviousPositionY
                v.stoneHit = 1

def nextLevel():
    global bg
    v.coal = 1

    if v.level == 4:
        bg = pygame.image.load(os.path.join("data\\background", "bg2.png")).convert()
    if v.level == 8:
        bg = pygame.image.load(os.path.join("data\\background", "bg3.png")).convert()
    if v.level == 12:
        bg = pygame.image.load(os.path.join("data\\background", "bg4.png")).convert()
    if v.level == 17:
        bg = pygame.image.load(os.path.join("data\\background", "bg5.png")).convert()
    if v.level == 22:
        bg = pygame.image.load(os.path.join("data\\background", "bg6.png")).convert()
    
    if v.level == v.LAST_LEVEL_NUMBER - 1:
        v.robboMsgNr = v.LAST_LEVEL_NUMBER - 1
    if v.level == v.LAST_LEVEL_NUMBER:
        v.robboMsgNr = v.LAST_LEVEL_NUMBER

    clearTiles()
    screen.blit(bg, (0,0))
    displayOnHUD()
    drawTiles()
    pygame.display.flip() 

    #endLevelExcessCoalCount()
    #global kamyki
    #v.level += 1
    #kamyki = arrays.dict_levels[v.level]
    
                  
        
def portalGlowAnim():
    screen.blit(bg, (v.portalGlowX*64,v.portalGlowY*64),(0,0,64,64)) 
    screen.blit(tileset, (v.portalGlowX*64,v.portalGlowY*64),(v.portalGlowFrame*64,11*64,64,64))     

def redCapacitorsAnim():
    i = 0
    k = 0
    if (v.redCapacitorAnimTick == v.CAPACITOR_TICK_TEMPO):
        for i in range (10):
            for k in range (7):
                if (v.collectiblesAnim[i][k] == 9):
                    screen.blit(bg, (i * 64,k * 64),(0,0,64,64))
                    screen.blit(tileset, (i * 64,k * 64),(v.redCapacitorAnimTileCheck*64,9*64,64,64))
    v.redCapacitorAnimTileCheck += 1
    if (v.redCapacitorAnimTileCheck == 7):
        v.redCapacitorAnimTileCheck = 0

def blueCapacitorsAnim():
    i = 0
    k = 0
    if (v.blueCapacitorAnimTick == v.CAPACITOR_TICK_TEMPO):
        for i in range (10):
            for k in range (7):
                if (v.collectiblesAnim[i][k] == 8):
                    screen.blit(bg, (i * 64,k * 64),(0,0,64,64))
                    screen.blit(tileset, (i * 64,k * 64),(v.blueCapacitorAnimTileCheck*64,8*64,64,64))
    v.blueCapacitorAnimTileCheck += 1
    if (v.blueCapacitorAnimTileCheck == 7):
        v.blueCapacitorAnimTileCheck = 0

def falconIdleAnimation():
    if (v.falconIdleControl == False):
        return
    elif (v.kierunek != 0 and v.stoneHit == 0):
        return
    
    if (v.falconIdle == v.falconIdleTempo * 1):
        v.idleFrame = 0
    elif (v.falconIdle == v.falconIdleTempo * 2):
        v.idleFrame = 1
    elif (v.falconIdle == v.falconIdleTempo * 3):
        v.idleFrame = 2
    elif (v.falconIdle == v.falconIdleTempo * 4):
        v.idleFrame = 3
    elif (v.falconIdle == v.falconIdleTempo * 5):
        v.idleFrame = 4
    elif (v.falconIdle == v.falconIdleTempo * 6):
        v.idleFrame = 5
    elif (v.falconIdle == v.falconIdleTempo * 7):
        v.idleFrame = 6
    elif (v.falconIdle == v.falconIdleTempo * 8):
        v.idleFrame = 7
        v.falconIdle = 0

    screen.blit(bg, (v.falconX*64,v.falconY*64),(0,0,64,64)) 
    screen.blit(tileset, (v.falconX*64,v.falconY*64),(v.idleFrame*64,v.falconFace+(6*64),64,64))

    



##### disable mouse 
pygame.event.set_blocked(pygame.MOUSEMOTION)

##### screen display after preparing everything
screen.blit(bg, (0,0))
displayOnHUD()

drawTiles()
pygame.display.flip()

##### MAIN LOOP
while run:
    pygame.display.flip()

    # handling with idle animations:
    v.portalGlowTick += 1
    if (v.portalGlowTick > v.PORTAL_TICK_TEMPO):
        v.portalGlowFrame += 1
        portalGlowAnim()
        v.portalGlowTick = 0
        if (v.portalGlowFrame == 7):
            v.portalGlowFrame = 0
    
    v.redCapacitorAnimTick += 1
    if (v.redCapacitorAnimTick > v.CAPACITOR_TICK_TEMPO):
        v.redCapacitorAnimTick = 0
    
    v.blueCapacitorAnimTick += 1
    if (v.blueCapacitorAnimTick > v.CAPACITOR_TICK_TEMPO):
        v.blueCapacitorAnimTick = 0

    redCapacitorsAnim()
    blueCapacitorsAnim()

    falconIdleAnimation()
    robboScrollUp()
    robboSays()
    robboScrollDown()

    if v.hudScrollingControl == v.ON:
        v.hudScrollingTick += 4 # This is the tempo of robboHUD scrolling up and down


    if v.gameStartProc == True:
        screen.blit(bg, (0,0))
        displayOnHUD()
        kamyki = arrays.dict_levels[1]
        drawTiles()
        v.gameStartProc = False

    
    

    if v.endLevelCheck == True:
        v.endLevelCheck = False
        nextLevel()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                v.kierunek = 1
            elif event.key == pygame.K_LEFT:
                v.kierunek = 2
            elif event.key == pygame.K_UP:
                v.kierunek = 3
            elif event.key == pygame.K_DOWN:
                v.kierunek = 4 
            elif event.key == pygame.K_ESCAPE:
                exec(open("menu.py").read()) 
            falconWholeFrameMovePrep()

    if (v.falconIdleControl == True):
        v.falconIdle += 1
    
    fpsClock.tick(FPS)    # wait vbl





    

