import pygame, sys, os, time

pygame.init()

run = True
screen = pygame.display.set_mode((640,512))
font = pygame.font.Font("data\\Topaz-8.ttf", 16)
position = 0

leakedTxt = [ "if (leaked capacitor == 2){", # message to print, too short to push into
    "amigaModeDestroy(); ", # seperate file, i think
    "}",
    "// WTF",
    "NO AMIGA SPIRIT FROM YOU I SMELL.",
    "LEAKED CAPACITOR NO GOOD IMPROVEMENT IS.",
    "SPACESHIP WICHER OF OURS YOU DESTROYED.",
    "MAY THE WEAKNESS OF ATARI BE WITH YOU.",
    "CHEATER. EAT COAL.",
    "(Fire or Return to continue)",
]

screen.fill((0, 85,85))  # screen bg color
for i in leakedTxt:      # simple loop to print message
    blitTxt = font.render(str(i), True, (0,153,153))
    screen.blit(blitTxt, (0,position))
    pygame.display.flip()
    position += 16
    time.sleep(0.1)



while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                exec(open('menu.py').read())
                #execfile('menu.py')
            elif event.key == pygame.K_ESCAPE:
                run = False