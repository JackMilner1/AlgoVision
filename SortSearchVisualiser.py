import pygame
import SearchingAlgorithms.BinarySearch as BinarySearch
import SearchingAlgorithms.LinearSearch as LinearSearch
import UIUtils.Buttons as Buttons
import UIUtils.Timer as Delay
import SortingAlgorithms.BubbleSort as BubbleSort
import Globals

pygame.init()

SCREEN_WIDTH = Globals.SCREEN_WIDTH
SCREEN_HEIGHT = Globals.SCREEN_HEIGHT

screen = Globals.screen
pygame.display.set_caption('Play')

def start(clickDelay = 0.2):
    running = True

    itemToSearch = 7

    items = []
    itemsList = []
    #solution = BinarySearch.BinarySearch(items,itemToSearch,0,len(items))
    solution = LinearSearch.LinearSearch(items,itemToSearch)
    currentStep = 0
    indexOfAns = solution[0]
    steps = solution[1]
    delayTimer = Delay.Timer(1)
    delayTimer.start()

    warningButton = Buttons.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.16,70,70,(43,43,55),"Preconditions not met for search")
    runButton = Buttons.Button(SCREEN_WIDTH * 0.85,SCREEN_HEIGHT * 0.7 - 100,90,90,(35, 35, 38),"Run")
    addItemButton = Buttons.Button(SCREEN_WIDTH * 0.85,SCREEN_HEIGHT * 0.7,90,90,(35, 35, 38),"Add Item")
    searchItemButton = Buttons.Button(SCREEN_WIDTH * 0.85 + 100,SCREEN_HEIGHT * 0.7,90,90,(35, 35, 38),"Search Item")
    sortItemsButton = Buttons.Button(SCREEN_WIDTH * 0.85,SCREEN_HEIGHT * 0.7+100,90,90,(35, 35, 38),"Sort Items")
    backButton = Buttons.Button((SCREEN_WIDTH - 70) * 0.97,(SCREEN_HEIGHT - 70) * 0.9,70,70,(81,81,88),"Back")

    text = ""
    runningSearchSimulation = False
    runningSortSimulation = False
    currentSimulation = "LINSEARCH" # options = BINSEARCH,LINSEARCH,MERGESORT,BUBBLESORT,QUICKSORT
    canRunSim = isValidSim(currentSimulation,items)

    pageClickDelay = Delay.Timer(clickDelay)
    pageClickDelay.start()

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

        pageClickDelay.update()
        canClickPage = pageClickDelay.timeRanOut

        screen.fill((43,43,55))

        drawTextBox(text,(SCREEN_WIDTH-200) * 0.5 , (SCREEN_HEIGHT-30) * 0.6,f"Add/search for item (current is {itemToSearch}): ")

        if addItemButton.drawButton(screen) and canClickPage:
            if validInput(text):
                items.append(int(text))
                runningSearchSimulation = False
                #solution = BinarySearch.BinarySearch(items,itemToSearch,0,len(items))
                solution = LinearSearch.LinearSearch(items,itemToSearch)
                indexOfAns = solution[0]
                steps = solution[1]
                canRunSim = isValidSim(currentSimulation,items)

            text = ""

        if searchItemButton.drawButton(screen) and canClickPage:
            if validInput(text):
                itemToSearch = int(text)
                runningSearchSimulation = False
                #solution = BinarySearch.BinarySearch(items,itemToSearch,0,len(items))
                solution = LinearSearch.LinearSearch(items,itemToSearch)
                indexOfAns = solution[0]
                steps = solution[1]
            text = ""
    

        if runButton.drawButton(screen) and canRunSim and canClickPage:
            runningSearchSimulation = True
            currentStep = 0
            #solution = BinarySearch.BinarySearch(items,itemToSearch,0,len(items))
            solution = LinearSearch.LinearSearch(items,itemToSearch)
            indexOfAns = solution[0]
            steps = solution[1]
            delayTimer.reset(1)

        if sortItemsButton.drawButton(screen) and canClickPage:
            runningSearchSimulation = False
            runningSortSimulation = True
            currentStep = 0
            itemsList, steps = BubbleSort.BubbleSort(items)

        if (runningSearchSimulation and canRunSim) or runningSortSimulation:

            delayTimer.update()

            if runningSortSimulation:
                if not canRunSim:
                    warningButton.drawButton(screen,(255,0,0))
                items = itemsList[currentStep]

            if delayTimer.timeRanOut and currentStep + 1 < len(steps) and currentStep != -1:
                currentStep += 1
                delayTimer.reset(1)
            elif delayTimer.timeRanOut and currentStep + 1 == len(steps):
                delayTimer.timeout()
                currentStep = -1
                runningSearchSimulation = False
                if runningSortSimulation:
                    runningSortSimulation = False
                    itemsList = []
                    canRunSim = True

            if currentStep != -1 and len(items) > 0:
                drawItems(items,steps[currentStep])
        elif not canRunSim:
            warningButton.drawButton(screen,(255,0,0))
            runningSearchSimulation = False
            drawItems(items)
        else:
            runningSearchSimulation = False
            drawItems(items)

        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))

        if backButton.drawButton(screen) and canClickPage:
            running = False

        pygame.display.flip()
        
    return True,False

def validInput(text):
    if text == "":
        return False
    
    for i in text:
        if not (i in ["0","1","2","3","4","5","6","7","8","9"]):
            return False
    
    return True

def isInOrder(items,text):
    if items[len(items) - 1] < int(text):
        return True
    else:
        return False
 
def isValidSim(currentSimulation,items):
    if currentSimulation == "BINSEARCH":
        if not BinarySearch.isInOrder(items):
            print("List not in order would you like to sort")
            return False
    if currentSimulation == "LINSEARCH":
        if len(items) == 0:
            return False
        
    return True

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
    
def draw_text(text,colour,rect,alignment="centre"):
    text_color = colour
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)

    if alignment == "centre":
        text_rect = text_surface.get_rect(center=rect.center)
    else:
        text_rect = text_surface.get_rect(midleft=(rect.midleft[0] + 10,rect.midleft[1]))

    screen.blit(text_surface, text_rect)

def drawTextBox(textSoFar,x,y,text):
    newRect = pygame.Rect(x,y,200,30)
    textRect = pygame.Rect(x,y - 24 ,200,24)
    pygame.draw.rect(screen,(50,50,50),newRect)
    draw_text(textSoFar,(255,255,255),newRect,"left")
    draw_text(text,(255,255,255),textRect)
