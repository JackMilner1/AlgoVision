import pygame
import os 
import UIUtils.Buttons as Button
import QueueTypes.Stack as Stack

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

STACK_UI_LENGTH = 400
STACK_UI_HEIGHT = 600
STACK_UI_EXTRA = 40
BOARD_START_X = int((SCREEN_WIDTH - STACK_UI_LENGTH) / 2)
BOARD_START_Y = int((SCREEN_HEIGHT - STACK_UI_HEIGHT) / 2) 
thicknessOfUI = 50

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Play')

def start():
    running = True

    pushButton = Button.Button(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.5,90,90,(35, 35, 38),"Push")
    popButton = Button.Button(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.5 + 95,90,90,(35, 35, 38),"Pop")
    resetButton = Button.Button(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.5 + (95 * 2),90,90,(35, 35, 38),"Reset")

    stack = Stack.Stack()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        drawStackUI()

        for i in range(stack.howManyItems()):
            drawItemInStack(i)

        if pushButton.drawButton(screen):
            if stack.howManyItems() < stack.maxItems():
                stack.push(3)
            else:
                print("Stack Overflow!")
        if resetButton.drawButton(screen):
            stack.clear()
        if popButton.drawButton(screen):
            if not stack.isEmpty():
                stack.pop()
            else: 
                print("Stack Underflow!")
        pygame.display.flip()
        
    pygame.quit()

def drawStackUI():
    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X,BOARD_START_Y,thicknessOfUI,STACK_UI_HEIGHT))
    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X + STACK_UI_LENGTH - thicknessOfUI,BOARD_START_Y,thicknessOfUI,STACK_UI_HEIGHT))

    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X - STACK_UI_EXTRA,BOARD_START_Y,STACK_UI_EXTRA,thicknessOfUI))
    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X + STACK_UI_LENGTH,BOARD_START_Y,STACK_UI_EXTRA,thicknessOfUI))

    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X,BOARD_START_Y + STACK_UI_HEIGHT - thicknessOfUI,STACK_UI_LENGTH,thicknessOfUI))

def drawItemInStack(itemNum):
    red = 255 - (itemNum * 26) 
    green = 0 + (itemNum * 26)
    pygame.draw.rect(screen,(clamp(red,0,255),clamp(green,0,255),0),(BOARD_START_X+thicknessOfUI,BOARD_START_Y + STACK_UI_HEIGHT - ((2 + itemNum) * thicknessOfUI),STACK_UI_LENGTH - (2 * thicknessOfUI),thicknessOfUI))

def clamp(value,lowerBound,upperBound): 
    if value < lowerBound:
        return lowerBound
    elif value > upperBound:
        return upperBound
    else:
        return value
    
start()