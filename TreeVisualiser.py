import pygame
import os 
import GraphClasses

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Play')

def start():
    running = True
    node1 = GraphClasses.VertexGeometry(1,400,500)
    node2 = GraphClasses.VertexGeometry(2,600,700)
    node3 = GraphClasses.VertexGeometry(3,600,300)
    node4 = GraphClasses.VertexGeometry(4,800,700)
    node5 = GraphClasses.VertexGeometry(5,800,300)
    node6 = GraphClasses.VertexGeometry(6,1000,700)
    node7 = GraphClasses.VertexGeometry(7,1000,300)
    node8 = GraphClasses.VertexGeometry(8,1200,500)
    #nodes = [(400,500),(600,700),(600,300),(800,700),(800,300),(1000,700),(1000,300),(1200,500)]
    node1.addEdge(screen,node2)
    node2.addEdge(screen,node8)
    node8.addEdge(screen,node3)
    nodes = [node1,node2,node3,node4,node5,node6,node7,node8]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        
        for node in nodes:
            node.drawEdges()

        for node in nodes:
            node.drawNode(screen)

        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()


start()