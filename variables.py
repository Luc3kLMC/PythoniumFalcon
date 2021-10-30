
MAP_TILE_HEIGHT = 6
MAP_TILE_WIDTH = 9
TILE_SIZE = 64
ANIM_FRAME_COUNT = 16
LAST_LEVEL_NUMBER = 28

ON = 1   # general purpose
OFF = 0

gameStartProc = True
keyPressed = False

# preparation & setup
level = 16
endLevelCheck = False
youWin = 0
HUDfontcolor = (0,153,153) 
startingCoal = 10
coal = startingCoal
excessCoal = 0
capacitors = 0
robboMsgCount = 0

robboMsgNr = 1

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

# hitting stone & frame handling 
stoneHit = 0
frameHit = 0
stoneHitAnimControl = 0
stoneHitAnimTick = 0
stoneHitAnimFrame = 0
oneFrameDirection = 0

# ship idle
falconIdle = 0
falconIdleTempo = 4
falconIdleControl = True
idleFrame = 0


# ship movement
falconX = 0
falconY = 0

falconPreviousPositionX = 0
falconPreviousPositionY = 0
kierunek = 0
falconFace = 0

krawedzX = 0
krawedzY = 0
uwPosX = 0
uwPosY = 0
tempX = 0
tempY = 0

flyingAnimControl = 0

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
CAPACITOR_TICK_TEMPO = 8
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
