import pygame
import Globals
import QueueTypes
import QueueTypes.FIFOQueue
import UIUtils.Timer as Delay

pygame.init()

SCREEN_WIDTH = Globals.SCREEN_WIDTH
SCREEN_HEIGHT = Globals.SCREEN_HEIGHT

screen = Globals.screen
pygame.display.set_caption('Play')

def start(clickDelay = 0.2):
    items = ["3","4","5","6"]
    queueType = "FIFO" # options [FIFO,PRIO,CIRCLE]
    running = True

    newQueue = QueueTypes.FIFOQueue.StandardQueue()
    newQueue.enqueue(5)

    pageClickDelay = Delay.Timer(clickDelay)
    pageClickDelay.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False,False

        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))

        if queueType != "CIRCLE":
            drawItems(items)
        pygame.display.flip()

    pygame.quit()

    return True,False

def drawItems(items,searched = []):
    searchCopy = searched.copy()
    numOfItems = len(items)
    itemWidth = 100
    itemHeight = 100
    spacing = 10
    startingX = (SCREEN_WIDTH - ((itemWidth + spacing) * numOfItems)) // 2
    for i in range(numOfItems):
        rect = pygame.Rect(startingX + ((itemWidth + spacing) * i),(SCREEN_HEIGHT - itemHeight) // 2, itemWidth,itemHeight)
        if items[i] in searchCopy:
            pygame.draw.rect(screen,(0,255,0),rect,border_radius=20)
            searchCopy.remove(items[i])
        else:
            pygame.draw.rect(screen,(0,0,0),rect,border_radius=20)
        draw_text(str(items[i]),(255,255,255),rect)

def drawCircularQueueItems(items):
    pass

def draw_text(text,colour,rect,alignment="centre"):
    text_color = colour
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)

    if alignment == "centre":
        text_rect = text_surface.get_rect(center=rect.center)
    else:
        text_rect = text_surface.get_rect(midleft=(rect.midleft[0] + 10,rect.midleft[1]))

    screen.blit(text_surface, text_rect)

start()