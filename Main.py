import pygame
import UIUtils.Buttons as Buttons
import GraphBuilder
import SortSearchVisualiser
import StackVisualiser
import TreeVisualiser
import Globals
import UIUtils.Timer as Delay

pygame.init()

SCREEN_WIDTH = Globals.SCREEN_WIDTH
SCREEN_HEIGHT = Globals.SCREEN_HEIGHT

screen = Globals.screen
pygame.display.set_caption('Menu')

def start(clickDelay = 0.2):

    running,option = mainMenu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((43,43,55))
        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))
        pygame.display.flip()

    pygame.quit()

def mainMenu(clickDelay = 0.2):
    running = True
    btnWidth = 250
    btnHeight = 75
    titleButton = Buttons.Button((SCREEN_WIDTH - ((SCREEN_WIDTH) * 0.5)) * 0.5,(SCREEN_HEIGHT - 150) * 0.25,((SCREEN_WIDTH) * 0.5),150,(43,43,55),"Algovision",128)
    startButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5,(SCREEN_HEIGHT - btnHeight) * 0.5,btnWidth,btnHeight,(81,81,88),"Start")
    quitButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5,(SCREEN_HEIGHT - btnHeight) * 0.5 + 75 + 40,btnWidth,btnHeight,(81,81,88),"Quit")
    inSelect = False

    pageClickDelay = Delay.Timer(clickDelay)
    pageClickDelay.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pageClickDelay.update()
        canClickPage = pageClickDelay.timeRanOut

        screen.fill((43,43,55))
        titleButton.drawButton(screen)

        if quitButton.drawButton(screen) and canClickPage:
            running = False

        if (startButton.drawButton(screen) or inSelect)  and canClickPage:
            running,inSelect = algoSelect()
            pageClickDelay.reset(clickDelay)

        pygame.display.flip()


    return running,0
    
def algoSelect(clickDelay = 0.2):
    running = True
    btnWidth = 250
    btnHeight = 75

    titleButton = Buttons.Button((SCREEN_WIDTH - ((SCREEN_WIDTH) * 0.5)) * 0.5,(SCREEN_HEIGHT - 150) * 0.25,((SCREEN_WIDTH) * 0.5),150,(43,43,55),"Select Topic",128)
    graphButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 - 140,(SCREEN_HEIGHT - btnHeight) * 0.5 - 37,btnWidth,btnHeight,(81,81,88),"Graphs")
    queuesButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 + 140,(SCREEN_HEIGHT - btnHeight) * 0.5 - 37,btnWidth,btnHeight,(81,81,88),"Queues")
    sortButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 - 140,(SCREEN_HEIGHT - btnHeight) * 0.5 + 75,btnWidth,btnHeight,(81,81,88),"Sort")
    treesButton = Buttons.Button((SCREEN_WIDTH - btnWidth) * 0.5 + 140,(SCREEN_HEIGHT - btnHeight) * 0.5 + +75,btnWidth,btnHeight,(81,81,88),"Trees")

    backButton = Buttons.Button((SCREEN_WIDTH - 250) * 0.97,(SCREEN_HEIGHT - 75) * 0.9,250,75,(81,81,88),"Back")

    pageClickDelay = Delay.Timer(clickDelay)
    pageClickDelay.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running,False
            
        pageClickDelay.update()
        canClickPage = pageClickDelay.timeRanOut

        screen.fill((43,43,55)) 

        titleButton.drawButton(screen)
        
        if graphButton.drawButton(screen) and canClickPage:
            running = GraphBuilder.start()[0]
            pageClickDelay.reset(clickDelay)
        if queuesButton.drawButton(screen) and canClickPage:
            running = SortSearchVisualiser.start()[0]
            pageClickDelay.reset(clickDelay)
        if sortButton.drawButton(screen) and canClickPage:
            running = SortSearchVisualiser.start()[0]
            pageClickDelay.reset(clickDelay)
        if treesButton.drawButton(screen) and canClickPage:
            running = TreeVisualiser.start()[0]
            pageClickDelay.reset(clickDelay)
        if not running:
            return False,False

        canClickPage = pageClickDelay.timeRanOut

        if backButton.drawButton(screen) and canClickPage:
            running = False

        pygame.display.flip()


    return True,False

start()