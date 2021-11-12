import pygame, sys, os, random, time
import arraysLevels as arrays
import robboTxt
from pygame.event import clear

import variables as v  
 

pygame.init()
random.seed(567) # stone-tile randomizer seed
stoneTileRandom = random.randint(1, 3)

screen = pygame.display.set_mode((640,512))
pygame.display.set_caption("PythoniumFalcon")
run = True
font = pygame.font.Font("data\\Topaz-8.ttf", 16)
#font = pygame.font.Font(os.path.join("data", "Topaz-8.ttf"), 16)

if v.thirdCheatEnabledWhenEqual3 != 3:
    tileset = pygame.image.load(os.path.join("data","tileset.png")).convert()
    tileset.set_colorkey((0,0,0))
    HUD = pygame.image.load(os.path.join("data", "HUD.png")).convert() # HUD image
elif v.thirdCheatEnabledWhenEqual3 == 3:
    tileset = pygame.image.load(os.path.join("data","tileset2.png")).convert()
    tileset.set_colorkey((0,0,0))
    HUD = pygame.image.load(os.path.join("data", "HUD2.png")).convert() # HUD image


bg = pygame.image.load(os.path.join("data\\background", "bg1.png")).convert() # background image nr 1
bgWithTile = pygame.image.load(os.path.join("data\\background", "bg1.png")).convert() # background image nr 1
#bgWithTile.set_colorkey((0,0,0))

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

def prepareFalconFlying():
    v.previousX = v.uwPosX
    v.previousY = v.uwPosY
    v.newPosX = v.uwPosX
    v.newPosY = v.uwPosY

    if v.kierunekHold == 1:
        v.tempX = v.falconX + 1
        v.uwPosX = v.tempX * 64
    if v.kierunekHold == 2:
        v.tempX = v.falconX - 1
        v.uwPosX = v.tempX * 64
    if v.kierunekHold == 3:
        v.tempY = v.falconY - 1
        v.uwPosY = v.tempY * 64
    if v.kierunekHold == 4:
        v.tempY = v.falconY + 1
        v.uwPosY = v.tempY * 64

def endFalconFlying():
    bgWithTile.blit(bg, (v.newPosX* v.TILE_SIZE,v.newPosY* v.TILE_SIZE),(v.newPosX* v.TILE_SIZE,v.newPosY* v.TILE_SIZE,64,64))
    if v.kierunekHold == 1:
        v.falconX = v.falconX + 1
    if v.kierunekHold == 2:
        v.falconX = v.falconX - 1
    if v.kierunekHold == 3:
        v.falconY = v.falconY - 1
    if v.kierunekHold == 4:
        v.falconY = v.falconY + 1

def blitFlyingFrame():
    screen.blit(bg, (v.previousX * v.TILE_SIZE, v.previousY * v.TILE_SIZE), pygame.Rect((v.previousX * v.TILE_SIZE, v.previousY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
    if (kamyki[v.tempX][v.tempY] > 3 and kamyki[v.tempX][v.tempY] != 10):
        screen.blit(bgWithTile, (v.newPosX* v.TILE_SIZE,v.newPosY* v.TILE_SIZE),(v.newPosX* v.TILE_SIZE,v.newPosY* v.TILE_SIZE,64,64))
    
    elif (kamyki[v.tempX][v.tempY] < 4):
        prevPosX = v.uwPosX
        prevPosY = v.uwPosY
        if v.kierunekHold == 1:
            prevPosX -= 2
        if v.kierunekHold == 2:
            prevPosX += 2
        if v.kierunekHold == 3:
            prevPosY += 2
        if v.kierunekHold == 4:
            prevPosY -= 2
        screen.blit(bg, (prevPosX, prevPosY), ((prevPosX, prevPosY), (v.TILE_SIZE,v.TILE_SIZE)))
        screen.blit(bg, (v.newPosX, v.newPosY),((v.newPosX, v.newPosY), (v.TILE_SIZE,v.TILE_SIZE)))

    screen.blit(tileset, (v.newPosX, v.newPosY),(v.flyingFrame*64,v.falconFace+(2*64),64,64))

def falconWholeFrameMovePrep():
    v.previousX = v.falconX
    v.previousY = v.falconY

    if v.kierunek == 1:
        v.falconX = v.falconX + 1
    elif v.kierunek == 2:
        v.falconX = v.falconX - 1
    elif v.kierunek == 3:
        v.falconY = v.falconY - 1
    elif v.kierunek == 4:
        v.falconY = v.falconY + 1

    
        

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
    global bgWithTile
    global bg 
    bgWithTile = bg
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
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(3 * 64,0,64,64))
            if kamyki[i][j] == 5:
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(4*64,0,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(4*64,0,64,64))
            if kamyki[i][j] == 6:                
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(5*64,0,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(5*64,0,64,64))
            if kamyki[i][j] == 7:               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(6*64,0,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(6*64,0,64,64))
            if kamyki[i][j] == 8:
                v.collectiblesAnim[i][j] = 8               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(0,64,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(0,64,64,64))
            if kamyki[i][j] == 9: 
                v.collectiblesAnim[i][j] = 9               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(64,64,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(64,64,64,64))
            if kamyki[i][j] == 10:
                v.portalGlowX = i
                v.portalGlowY = j               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(128,64,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(128,64,64,64))
            if kamyki[i][j] == 11:               
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(192,64,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(192,64,64,64))
            if kamyki[i][j] == 12:
                screen.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(256,64,64,64))
                bgWithTile.blit(tileset, (i * v.TILE_SIZE, j * v.TILE_SIZE),(256,64,64,64))
    
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
    displayOnHUD()
    
def falconHittingStone():
    if v.stoneHitAnimControl != 1:
        return
    
    posX = v.falconX * 64
    posY = v.falconY * 64
    #v.oneFrameDirection = v.kierunekHold

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

    screen.blit(bg, (posX, posY),((posX, posY), (v.TILE_SIZE,v.TILE_SIZE)))
    screen.blit(tileset, (posX,posY),(v.stoneHitAnimFrame * 64,v.falconFace + 128,64,64))   

def levelScore():
    if (v.levelScoreControl == v.LEVEL_SCORE_OFF):
        return
    if (v.coal == 1 and v.levelScoreControl == v.LEVEL_SCORE_COUNT):
        v.levelScoreControl = v.LEVEL_SCORE_PORTAL_OPEN
        v.falconIdleControl = 0
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
        v.falconIdleControl = 1
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
        v.previousY = 0
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
        #v.hudScrollingControl = v.ON
        #v.hudScrollingTick = 0 

def robboScrollDown():
    if v.robboMsgCtrl != v.SCROLL_DOWN:
        return
    
    if v.hudScrollingControl == v.ON:
        screen.blit(HUD, (0,448))
        screen.blit(robboHUD, (0,448 + v.hudScrollingTick))
     
    if v.hudScrollingTick >= 64:     
        v.robboMsgCtrl = v.SCROLL_OFF
        v.hudScrollingTick = 0
        v.hudScrollingControl = v.OFF
        displayOnHUD()
    
def falconWholeFrameMoveBlit():
    screen.blit(bg, (v.previousX * v.TILE_SIZE, v.previousY * v.TILE_SIZE), pygame.Rect((v.previousX * v.TILE_SIZE, v.previousY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
    screen.blit(tileset, (v.falconX * v.TILE_SIZE,v.falconY * v.TILE_SIZE),(0,128,64,64))   
    #pygame.display.flip()
    
def falconCollisionCheck():
    if v.stoneHit == 1:
        v.stoneHitAnimControl = 1
        v.falconIdleControl = 0
    
        if v.kierunekHold == 1:
            v.krawedzX -= 1
        if v.kierunekHold == 2:
            v.krawedzX += 1
        if v.kierunekHold == 3:
            v.krawedzY += 1
        if v.kierunekHold == 4:
            v.krawedzY -= 1

        v.stoneHit = 0
        return
    
    if v.frameHit == 1:
        v.stoneHitAnimControl = 1
        v.falconIdleControl = 0
        v.frameHit = 0
        return

    prepareFalconFlying()
    v.flyingAnimControl = 1 


    #if v.falconX == v.MAP_TILE_WIDTH + 1:    # RIGHT BORDER
    #    v.falconX = v.MAP_TILE_WIDTH
    #    v.frameHit = 1
    #elif v.falconX == -1:                   # LEFT BORDER
    #    v.falconX = 0
    #    v.frameHit = 1
    #elif v.falconY == v.MAP_TILE_HEIGHT + 1:  # DOWN BORDER
    #    v.falconY = v.MAP_TILE_HEIGHT
    #    v.frameHit = 1
    #elif v.falconY == -1:                      # UP BORDER
    #    v.falconY = 0
    #    v.frameHit = 1

def czyRamka():
    if v.kierunekHold == 1:
        v.krawedzX = v.falconX + 1
        if v.krawedzX == 10:
            v.krawedzX = 9
            v.falconX = 9
            v.frameHit = 1
    if v.kierunekHold == 2:
        v.krawedzX = v.falconX - 1
        if v.krawedzX == -1:
            v.krawedzX = 0
            v.falconX = 0
            v.frameHit = 1
    if v.kierunekHold == 3:
        v.krawedzY = v.falconY - 1
        if v.krawedzY == -1:
            v.krawedzY = 0
            v.falconY = 0
            v.frameHit = 1
    if v.kierunekHold == 4:
        v.krawedzY = v.falconY + 1
        if v.krawedzY == 7:
            v.krawedzY = 6
            v.falconY = 6
            v.frameHit = 1

def isThisStone():
    stoneX = 0
    stoneY = 0

    if v.kierunekHold == 1:
        stoneX = v.falconX + 1
        if kamyki[stoneX][v.falconY] == 3:
            v.stoneHit = 1
    if v.kierunekHold == 2:
        stoneX = v.falconX - 1
        if kamyki[stoneX][v.falconY] == 3:
            v.stoneHit = 1
    if v.kierunekHold == 3:
        stoneY = v.falconY - 1
        if kamyki[v.falconX][stoneY] == 3:
            v.stoneHit = 1
    if v.kierunekHold == 4:
        stoneY = v.falconY + 1
        if kamyki[v.falconX][stoneY] == 3:
            v.stoneHit = 1


    #for i in range(len(kamyki)):
    #    for j in range(len(kamyki[i])): 
    #        if kamyki[v.falconX][v.falconY] == 3:
    #            v.falconX = v.previousX
    #            v.falconY = v.previousY
    #            v.stoneHit = 1

def nextLevel():
    global bg, bgWithTile
    v.coal = 1

    if v.level == 4:
        bg = pygame.image.load(os.path.join("data\\background", "bg2.png")).convert()
        bgWithTile = pygame.image.load(os.path.join("data\\background", "bg2.png")).convert()
    if v.level == 8:
        bg = pygame.image.load(os.path.join("data\\background", "bg3.png")).convert()
        bgWithTile = pygame.image.load(os.path.join("data\\background", "bg3.png")).convert()
    if v.level == 12:
        bg = pygame.image.load(os.path.join("data\\background", "bg4.png")).convert()
        bgWithTile = pygame.image.load(os.path.join("data\\background", "bg4.png")).convert()
    if v.level == 17:
        bg = pygame.image.load(os.path.join("data\\background", "bg5.png")).convert()
        bgWithTile = pygame.image.load(os.path.join("data\\background", "bg5.png")).convert()
    if v.level == 22:
        bg = pygame.image.load(os.path.join("data\\background", "bg6.png")).convert()
        bgWithTile = pygame.image.load(os.path.join("data\\background", "bg6.png")).convert()
    
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
    if (v.falconIdleControl == 0):
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

    #bg = pygame.image.load(os.path.join("data\\background", "bg1.png")).convert() # background image nr 1
    screen.blit(bg, (v.falconX*64,v.falconY*64),(v.falconX*64,v.falconY*64,64,64)) 
    screen.blit(tileset, (v.falconX*64,v.falconY*64),(v.idleFrame*64,v.falconFace+(6*64),64,64))

def falconFlying():
    if v.flyingAnimControl == 0:
        return

    if v.flyingAnimControl == 1:
        v.falconIdleControl = 0
        v.flyingAnimControl = 3
        screen.blit(bg, (v.newPosX, v.newPosY),((v.newPosX, v.newPosY), (v.TILE_SIZE,v.TILE_SIZE)))

        if v.kierunekHold == 1:    
            v.newPosX += 2
        if v.kierunekHold == 2:    
            v.newPosX -= 2
        if v.kierunekHold == 3:    
            v.newPosY -= 2
        if v.kierunekHold == 4:    
            v.newPosY += 2

        if v.flyingTick == 4:
            v.flyingFrame = 0

        if (v.flyingTick == 8 or v.flyingTick == 12 or v.flyingTick == 16 or v.flyingTick == 20 or v.flyingTick == 24 or v.flyingTick == 28 or v.flyingTick == 32):
            v.flyingFrame += 1

        blitFlyingFrame()

        if v.flyingTick >= 32:
            v.flyingTick = 0
            v.flyingAnimControl = 2
    
    if v.flyingAnimControl == 2:
        screen.blit(bg, (v.previousX * v.TILE_SIZE, v.previousY * v.TILE_SIZE), pygame.Rect((v.previousX * v.TILE_SIZE, v.previousY * v.TILE_SIZE), (v.TILE_SIZE,v.TILE_SIZE)))
        endFalconFlying()
        coalAndCollect()
        v.flyingAnimControl = 0
        v. falconIdleControl = 1




##### disable mouse 
pygame.event.set_blocked(pygame.MOUSEMOTION)

##### screen display after preparing everything
screen.blit(bg, (0,0))
displayOnHUD()

drawTiles()
pygame.display.flip()







    

