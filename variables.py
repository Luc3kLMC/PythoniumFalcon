
MAP_TILE_HEIGHT = 6
MAP_TILE_WIDTH = 9
TILE_SIZE = 64
ANIM_FRAME_COUNT = 16
LAST_LEVEL_NUMBER = 28

gameStartProc = True
keyPressed = False

# preparation & setup
level = 1
endLevelCheck = False
startingCoal = 10
coal = startingCoal
excessCoal = 0
capacitors = 0
robboMsgCount = 0
robboMsgCtrl = 0
robboMsgNr = 1

# array initialization for capacitors animation
w, h = 7, 10
collectiblesAnim = [[0 for x in range(w)] for y in range(h)]

# hitting stone 
stoneHit = 0

# ship idle
falconIdle = 0
falconIdleTempo = 4
falconIdleControl = True
idleFrame = 0


# ship movement
falconPositionX = 0
falconPositionY = 0

falconPreviousPositionX = 0
falconPreviousPositionY = 0
kierunek = 0
falconFace = 0

# portal animation 
portalGlowX = 0
portalGlowY = 0
PORTAL_TICK_TEMPO = 4
portalGlowTick = 0
portalGlowFrame = 0

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
