import pygame
import UIUtils.Buttons as Buttons
import GraphBuilder
import SortSearchVisualiser
import StackVisualiser
import TreeVisualiser
import Globals

pygame.init()

SCREEN_WIDTH = Globals.SCREEN_WIDTH
SCREEN_HEIGHT = Globals.SCREEN_HEIGHT

screen = Globals.screen
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
    startButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5,(SCREEN_HEIGHT - btnHeight) * 0.5,btnWidth,btnHeight,(81,81,88),"Start")
    quitButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5,(SCREEN_HEIGHT - btnHeight) * 0.5 + 75 + 40,btnWidth,btnHeight,(81,81,88),"Quit")
    inSelect = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        titleButton.drawButton(screen)

        if quitButton.drawButton(screen):
            running = False

        if startButton.drawButton(screen) or inSelect:
            running,inSelect = algoSelect()

        pygame.display.flip()


    return running,0
    
def algoSelect():
    running = True
    btnWidth = 250
    btnHeight = 75

    titleButton = Buttons.Button((SCREEN_WIDTH - ((SCREEN_WIDTH) * 0.5)) * 0.5,(SCREEN_HEIGHT - 150) * 0.25,((SCREEN_WIDTH) * 0.5),150,(43,43,55),"Select Topic",128)
    graphButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 - 140,(SCREEN_HEIGHT - btnHeight) * 0.5 - 37,btnWidth,btnHeight,(81,81,88),"Graphs")
    queuesButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 + 140,(SCREEN_HEIGHT - btnHeight) * 0.5 - 37,btnWidth,btnHeight,(81,81,88),"Queues")
    sortButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 - 140,(SCREEN_HEIGHT - btnHeight) * 0.5 + 75,btnWidth,btnHeight,(81,81,88),"Sort")
    treesButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 + 140,(SCREEN_HEIGHT - btnHeight) * 0.5 + +75,btnWidth,btnHeight,(81,81,88),"Trees")

    backButton = Buttons.Button((SCREEN_WIDTH - 250) * 0.97,(SCREEN_HEIGHT - 75) * 0.9,250,75,(81,81,88),"Back")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running,0

        screen.fill((43,43,55)) 

        titleButton.drawButton(screen)
        
        if graphButton.drawButton(screen):
            return GraphBuilder.start()
        if queuesButton.drawButton(screen):
            return SortSearchVisualiser.start()
        if sortButton.drawButton(screen):
            return SortSearchVisualiser.start()
        if treesButton.drawButton(screen):
            return TreeVisualiser.start()

        if backButton.drawButton(screen):
            running = False

        pygame.display.flip()


    return True,False

start()