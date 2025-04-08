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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        pygame.draw.line(screen,(0,0,0),(450,550), (650,750),width=10)
        pygame.draw.line(screen,(0,0,0),(450,550), (650,350),width=10)
        pygame.draw.line(screen,(0,0,0),(450,550), (850,750),width=10)
        pygame.draw.line(screen,(0,0,0),(450,550), (850,350),width=10)
        pygame.draw.line(screen,(0,0,0),(450,550), (1200,550),width=10)
        drawNode(400,500)
        drawNode(600,700)
        drawNode(600,300)
        drawNode(800,700)
        drawNode(800,300)
        drawNode(1000,700)
        drawNode(1000,300)
        drawNode(1200,500)
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()

def drawNode(x,y):
    pygame.draw.rect(screen,(0,0,0),(x,y,100,100),border_radius=100)
    pygame.draw.rect(screen,(35, 35, 38),(x + 5,y + 5,90,90),border_radius=100,width=5)
  
start()