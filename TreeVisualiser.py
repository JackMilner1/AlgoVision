import pygame
import os 
import GraphClasses
import UIUtils.Buttons as Button

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Play')

def start():
    running = True
    nodes = []

    nodeFromSelected = None

    screenClickArea = Button.Button(0,SCREEN_HEIGHT*0.15,SCREEN_WIDTH,SCREEN_HEIGHT*0.85,(43,43,55))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if screenClickArea.drawButton(screen):
            nodeFromSelected = manageScreenClick(nodes,nodeFromSelected)
        
        for node in nodes:
            node.drawEdges()

        for node in nodes:
            node.drawNode(screen)

        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()

def manageScreenClick(nodes,nodeFromSelected):
    coords = pygame.mouse.get_pos()
    x = coords[0] - 50
    y = coords[1] - 50
    canPlace = True
    for node in nodes:
        if (x - 100 < node.x < x + 100) and (y - 100 < node.y < y + 100):
            canPlace = False
            if nodeFromSelected == None:
                nodeFromSelected = node
            else:
                # draw connection 
                nodeFromSelected.addEdge(screen,node)
                nodeFromSelected = None

    if canPlace:
        newNode = GraphClasses.VertexGeometry(len(nodes) + 1,x,y)
        nodes.append(newNode)

    return nodeFromSelected

start()