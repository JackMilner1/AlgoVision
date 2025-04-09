import pygame
import os 

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Play')

def start():
    running = True
    nodes = [(400,500),(600,700),(600,300),(800,700),(800,300),(1000,700),(1000,300),(1200,500)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        
        for node1 in nodes:
            for node2 in nodes:
                connectNodes(node1,node2)

        for i in range(len(nodes)):
            node = nodes[i]
            drawNode(node,i)

        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()

def drawNode(xy,text):
    x,y = xy
    nodeRect = pygame.Rect(x,y,100,100)
    pygame.draw.rect(screen,(0,0,0),nodeRect,border_radius=100)
    pygame.draw.rect(screen,(35, 35, 38),(x + 5,y + 5,90,90),border_radius=100,width=5)
    draw_text(str(text),nodeRect)

def connectNodes(node1,node2):
    pygame.draw.line(screen,(0,0,0),(node1[0] + 50,node1[1] + 50), (node2[0] + 50,node2[1] + 50),width=10)

def draw_text(text, button_rect):
    text_color = (255, 255, 255)
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    
start()