import pygame
import SearchingAlgorithms.BinarySearch as BinarySearch
import SearchingAlgorithms.LinearSearch as LinearSearch
import UIUtils.Timer as Delay
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

    items = [1,4,6,7,9,12,13,16,70,104,108]
    #solution = BinarySearch.BinarySearch(items,7,0,len(items))
    solution = LinearSearch.LinearSearch(items,70)
    currentStep = 0
    indexOfAns = solution[0]
    steps = solution[1]
    delayTimer = Delay.Timer(1)
    delayTimer.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))

        delayTimer.update()

        if delayTimer.timeRanOut and currentStep + 1 < len(steps):
            currentStep += 1
            delayTimer.reset(1)
        elif delayTimer.timeRanOut and currentStep + 1 == len(steps):
            currentStep = 0
            delayTimer.reset(1)

        drawItems(items,steps[currentStep])

        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()

def drawItems(items,searched = []):
    numOfItems = len(items)
    itemWidth = 100
    itemHeight = 100
    spacing = 10
    startingX = (SCREEN_WIDTH - ((itemWidth + spacing) * numOfItems)) // 2
    for i in range(numOfItems):
        rect = pygame.Rect(startingX + ((itemWidth + spacing) * i),(SCREEN_HEIGHT - itemHeight) // 2, itemWidth,itemHeight)
        if items[i] in searched:
            pygame.draw.rect(screen,(0,255,0),rect,border_radius=20)
        else:
            pygame.draw.rect(screen,(0,0,0),rect,border_radius=20)
        draw_text(str(items[i]),(255,255,255),rect)
    
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