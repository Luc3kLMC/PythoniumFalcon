
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


# ship movement
falconPositionX = 0
falconPositionY = 0

falconPreviousPositionX = 0
falconPreviousPositionY = 0
movementDirection = 0

# portal animation 
portalGlowX = 0
portalGlowY = 0
PORTAL_TICK_TEMPO = 4
portalGlowTick = 0
portalGlowFrame = 0



amigaMode = 0
