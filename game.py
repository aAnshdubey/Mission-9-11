import random # For generating random number
import sys #we will use sys.exit to exit the program
import pygame
from pygame.locals import * #Basic pygame imports

#global variable for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) 
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'flappy/sprites/aeroplane.png'
BACKGROUND = 'flappy/sprites/background.png'
PIPE = 'flappy/sprites/building.png'

def welcomescreen():
    """Shows welcome image on the screen"""
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    welcomex = int((SCREENWIDTH - GAME_SPRITES['welcome'].get_width())/2)
    welcomey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            


if __name__ == "__main__":
    #This will be the main point from where our game start
    pygame.init() #initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('911 by TECH VISIONARIES')
    GAME_SPRITES['number'] = (
        pygame.image.load('flappy/sprites/0.png').convert_alpha(),
        pygame.image.load('flappy/sprites/1.png').convert_alpha(),
        pygame.image.load('flappy/sprites/2.png').convert_alpha(),
        pygame.image.load('flappy/sprites/3.png').convert_alpha(),
        pygame.image.load('flappy/sprites/4.png').convert_alpha(),
        pygame.image.load('flappy/sprites/5.png').convert_alpha(),
        pygame.image.load('flappy/sprites/6.png').convert_alpha(),
        pygame.image.load('flappy/sprites/7.png').convert_alpha(),
        pygame.image.load('flappy/sprites/8.png').convert_alpha(),
        pygame.image.load('flappy/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['welcome'] =pygame.image.load('flappy/sprites/welcome.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('flappy/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha()
    )

    # #game sounds
    # GAME_SOUNDS['die'] = pygame.mixer.Sound()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows  welcome screen to the user until he press a button
        mainGame() # This is the main game function
