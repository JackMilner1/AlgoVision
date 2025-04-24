import pygame
import UIUtils.Buttons as Buttons
import os 

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT- 50),pygame.RESIZABLE)
pygame.display.set_caption('Menu')

def start():

    running,option = mainMenu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()

def mainMenu():
    running = True
    btnWidth = 250
    btnHeight = 75
    titleButton = Buttons.Button((SCREEN_WIDTH - ((SCREEN_WIDTH) * 0.5)) * 0.5,(SCREEN_HEIGHT - 150) * 0.25,((SCREEN_WIDTH) * 0.5),150,(43,43,55),"Algovision",128)
    startButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5,(SCREEN_HEIGHT - btnHeight) * 0.6,btnWidth,btnHeight,(81,81,88),"Start")
    quitButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5,(SCREEN_HEIGHT - btnHeight) * 0.6 + 75 + 40,btnWidth,btnHeight,(81,81,88),"Quit")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        titleButton.drawButton(screen)

        if startButton.drawButton(screen):
            print("start")

        if quitButton.drawButton(screen):
            running = False

        pygame.display.flip()


    return running,0
    
start()