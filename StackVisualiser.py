import pygame
import UIUtils.Buttons as Button
import QueueTypes.Stack as Stack
import UIUtils.Timer as Timer
import Globals

pygame.init()

SCREEN_WIDTH = Globals.SCREEN_WIDTH
SCREEN_HEIGHT = Globals.SCREEN_HEIGHT

STACK_UI_LENGTH = 400
STACK_UI_HEIGHT = 600
STACK_UI_EXTRA = 40
BOARD_START_X = int((SCREEN_WIDTH - STACK_UI_LENGTH) / 2)
BOARD_START_Y = int((SCREEN_HEIGHT - STACK_UI_HEIGHT) / 2) 
thicknessOfUI = 50

screen = Globals.screen
pygame.display.set_caption('Play')

def start():
    running = True
    warningButton = Button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.16,70,70,(43,43,55),"")
    pushButton = Button.Button(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.5,90,90,(35, 35, 38),"Push")
    popButton = Button.Button(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.5 + 95,90,90,(35, 35, 38),"Pop")
    resetButton = Button.Button(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.5 + (95 * 2),90,90,(35, 35, 38),"Reset")
    backButton = Button.Button((SCREEN_WIDTH - 250) * 0.97,(SCREEN_HEIGHT - 75) * 0.9,250,75,(81,81,88),"Back")
    warningTimer = Timer.Timer(8)
    stack = Stack.Stack()
    text = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False,False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode


        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        drawStackUI()

        drawTextBox(text)
        
        if warningTimer.active:
            warningTimer.update()
            warningButton.drawButton(screen,(255,0,0))

        for i in range(stack.howManyItems()):
            drawItemInStack(i,stack)

        if pushButton.drawButton(screen):
            if stack.howManyItems() < stack.maxItems():
                stack.push(text)
                text = ""
            else:
                #print("Stack Overflow!")
                warningButton.changeText("Stack Overflow!")
                warningTimer.reset(3)
        if resetButton.drawButton(screen):
            text = ""
            stack.clear()
        if popButton.drawButton(screen):
            if not stack.isEmpty():
                stack.pop()
            else: 
                #print("Stack Underflow!")
                warningButton.changeText("Stack Underflow!")
                warningTimer.reset(3)

        if backButton.drawButton(screen):
            running = False
        pygame.display.flip()
    return True,False

def drawStackUI():
    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X,BOARD_START_Y,thicknessOfUI,STACK_UI_HEIGHT))
    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X + STACK_UI_LENGTH - thicknessOfUI,BOARD_START_Y,thicknessOfUI,STACK_UI_HEIGHT))

    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X - STACK_UI_EXTRA,BOARD_START_Y,STACK_UI_EXTRA,thicknessOfUI))
    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X + STACK_UI_LENGTH,BOARD_START_Y,STACK_UI_EXTRA,thicknessOfUI))

    pygame.draw.rect(screen,(0,0,0),(BOARD_START_X,BOARD_START_Y + STACK_UI_HEIGHT - thicknessOfUI,STACK_UI_LENGTH,thicknessOfUI))

def drawItemInStack(itemNum,stack):
    red = 255 - (itemNum * 26) 
    green = 0 + (itemNum * 26)
    newRect = pygame.Rect(BOARD_START_X+thicknessOfUI,BOARD_START_Y + STACK_UI_HEIGHT - ((2 + itemNum) * thicknessOfUI),STACK_UI_LENGTH - (2 * thicknessOfUI),thicknessOfUI)
    pygame.draw.rect(screen,(clamp(red,0,255),clamp(green,0,255),0),newRect)
    draw_text(stack.getElements()[-1 - itemNum],(255,255,255),newRect)

def clamp(value,lowerBound,upperBound): 
    if value < lowerBound:
        return lowerBound
    elif value > upperBound:
        return upperBound
    else:
        return value

def draw_text(text,colour,rect,alignment="centre"):
    text_color = colour
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)

    if alignment == "centre":
        text_rect = text_surface.get_rect(center=rect.center)
    else:
        text_rect = text_surface.get_rect(midleft=(rect.midleft[0] + 10,rect.midleft[1]))
    
    
    screen.blit(text_surface, text_rect)

def drawTextBox(textSoFar):
    newRect = pygame.Rect(SCREEN_WIDTH * 0.7 , SCREEN_HEIGHT * 0.34 ,200,30)
    textRect = pygame.Rect(SCREEN_WIDTH * 0.7 , SCREEN_HEIGHT * 0.34 - 24 ,200,24)
    pygame.draw.rect(screen,(50,50,50),newRect)
    draw_text(textSoFar,(255,255,255),newRect,"left")
    draw_text("Text to push to stack: ",(255,255,255),textRect)
