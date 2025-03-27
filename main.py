import pygame
import os

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Play')

boardWidth = 20
boardHeight = 10
WHITE_SQUARE_COLOUR = (70,70,89)
SQUARE_SIZE = 80
SPACING = 10
BOARD_START_X = int((SCREEN_WIDTH - ((SQUARE_SIZE + SPACING) * boardWidth)) / 2)
BOARD_START_Y = int((SCREEN_HEIGHT - ((SQUARE_SIZE + SPACING) * boardHeight)) / 2) + 10


def drawSquares():
    for i in range(boardHeight):
        for j in range(boardWidth):
            boardx = BOARD_START_X + (SQUARE_SIZE * j)
            boardy = BOARD_START_Y + (SQUARE_SIZE * i)
            pygame.draw.rect(screen,(WHITE_SQUARE_COLOUR),(boardx + (SPACING * j),boardy + (SPACING * i),SQUARE_SIZE,SQUARE_SIZE))
             
def start():
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.08))
        drawSquares()

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()


start()
