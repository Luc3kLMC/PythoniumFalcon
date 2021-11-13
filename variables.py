import robboTxt

MAP_TILE_HEIGHT = 6
MAP_TILE_WIDTH = 9
TILE_SIZE = 64
ANIM_FRAME_COUNT = 16
LAST_LEVEL_NUMBER = 28

### IMPORTANT 
### RUN STATES FOR GENERAL STATE MACHINE:
STATE_MENU = 1
STATE_CREDITS = 2
STATE_GAME = 3
STATE_INTRO = 4
STATE_SCORE = 5
STATE_GAMEOVER = 6
STATE_LEAKED_GAME_OVER = 7
generalState = STATE_MENU
menuBlit = 0
scoreBlit = 0
gameoverBlit = 0

ON = 1   # general purpose
OFF = 0

gameStartProc = True
keyPressed = False

# preparation & setup
level = 1
endLevelCheck = False
youWin = 0
HUDfontcolor = (0,153,153) 
startingCoal = 10
coal = startingCoal
excessCoal = 0
capacitors = 0
robboMsgCount = 0

robboMsgNr = 0

# array initialization for capacitors animation
w, h = 7, 10
collectiblesAnim = [[0 for x in range(w)] for y in range(h)]

# HUD operations (scroll up, down, display robbo msg)
SCROLL_OFF = 0
SCROLL_UP = 1
SCROLL_DOWN = 2
SCROLL_DISPLAY = 3

hudScrollingControl = 0
hudScrollingTick = 0
robboMsgCtrl = SCROLL_OFF
robboMessages = robboTxt.dict_robboTxt[robboMsgNr]

# hitting stone & frame handling 
stoneHit = 0
frameHit = 0
stoneHitAnimControl = 0
stoneHitAnimTick = 0
stoneHitAnimFrame = 0
oneFrameDirection = 0

# ship idle
falconIdle = 1
falconIdleTempo = 4
falconIdleControl = 1
idleFrame = 0


# ship movement
falconX = 0
falconY = 0

previousX = 0
previousY = 0
kierunek = 0
kierunekHold = 0

falconFace = 0

krawedzX = 0
krawedzY = 0
uwPosX = 0
uwPosY = 0

newPosX = 0
newPosY = 0
tempX = 0
tempY = 0

flyingAnimControl = 0
flyingTick = 0
flyingFrame = 0


# portal animation 
portalGlowX = 0
portalGlowY = 0
PORTAL_TICK_TEMPO = 4
portalGlowTick = 0
portalGlowFrame = 0
portalAnimTick = 0

# R U capacitors animation
redCapacitorAnimTick = 0
blueCapacitorAnimTick = 0
CAPACITOR_TICK_TEMPO = 2
redCapacitorAnimTileCheck = 0
blueCapacitorAnimTileCheck = 0

# amiga mode 
AMIGA_MODE_OFF = 0
AMIGA_MODE_ON = 1
AMIGA_MODE_CHECK = 2
amigaMode = 0

# levels and score handling
levelScoreControl = 0
levelScoreTick = 0
levelScoreTempo = 8
levelAnimFrame = 0
LEVEL_SCORE_OFF = 0
LEVEL_SCORE_COUNT = 1
LEVEL_SCORE_PORTAL_OPEN = 2
LEVEL_SCORE_PORTAL_ANIM = 3
LEVEL_SCORE_PORTAL_CLOSE = 4
LEVEL_SCORE_END = 5
LEVEL_SCORE_NOCOAL = 6

# cheatcodes handling
firstCheatEnabledWhenEqual3 = 0
secondCheatEnabledWhenEqual3 = 0
thirdCheatEnabledWhenEqual3 = 0

# credits kinda enum style 
STATE_LMC_FADE_IN = 1
STATE_LMC_FADE_OUT = 2
STATE_ACE_FADE_IN = 3
STATE_ACE_FADE_OUT = 4
STATE_CREDITS_TEXT= 5

fadeTick = 0
stateActual = STATE_LMC_FADE_IN  # controling the phase we're already in
creditsDisplayed = 0
creditsPosition = 0

# intro variables
introPosition = 0
introPageControl = 0
