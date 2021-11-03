import pygame, sys, os, random, time

from pygame.event import clear
import arraysLevels as arrays
import variables as v  
import robboTxt 

pygame.init()
FPS = 50
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



#screen.blit(bg, (0,0))
bg.blit(tileset, (0, 0),(0,(2*64),64,64))
screen.blit(bg, (0,0))
pygame.display.flip()

time.sleep(2)