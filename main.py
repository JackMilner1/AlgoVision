import pygame
import os
import graph
import UtilsUI as utils

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Play')

boardWidth = 40
boardHeight = 20
WHITE_SQUARE_COLOUR = (70,70,89)
SQUARE_SIZE = 30
SPACING = 10
BOARD_START_X = int((SCREEN_WIDTH - ((SQUARE_SIZE + SPACING) * boardWidth)) / 2)
BOARD_START_Y = int((SCREEN_HEIGHT - ((SQUARE_SIZE + SPACING) * boardHeight)) / 2) + 10

newGraph = graph.Graph(boardWidth,boardHeight)
vertices = newGraph.getVertices()
graphUI = []

def drawSquares():
    allVertices = newGraph.getVertices()
    for i in range(boardHeight):
        for j in range(boardWidth):
            index = (i * boardWidth) + j
            boardx = BOARD_START_X + (SQUARE_SIZE * j)
            boardy = BOARD_START_Y + (SQUARE_SIZE * i)
            rect = pygame.Rect(boardx + (SPACING * j),boardy + (SPACING * i),SQUARE_SIZE,SQUARE_SIZE)
            #pygame.draw.rect(screen,(WHITE_SQUARE_COLOUR),rect)
            newSquare = utils.GridSquare(allVertices[index], boardx + (SPACING * j),boardy + (SPACING * i),SQUARE_SIZE,SQUARE_SIZE,WHITE_SQUARE_COLOUR)
            graphUI.append(newSquare)

            # -- code for displaying connections -- 
            #draw_text(str(allVertices[index].getID()),rect)
            #draw_text(str(allVertices[index].getNeighbours()),pygame.Rect(boardx + (SPACING * j),boardy + (SPACING * i) + 20,SQUARE_SIZE,SQUARE_SIZE))
             
def start():
    running = True
    drawSquares()
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.08))

        # RENDER YOUR GAME HERE
        for i in graphUI:
            if i.drawButton(screen):
                vert = i.getClass()
                print(f"Node Number : {vert.getID()} \nAll neigbours : {vert.getNeighbours()}")

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()

def draw_text(text, button_rect):
    text_color = (255, 255, 255)
    font = pygame.font.Font(None, 13)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

start()
