import pygame
import GraphClasses
import UIUtils.Buttons as Button
import Globals
import UIUtils.Timer as Delay
import Traversals.DFS as DFS
pygame.init()

SCREEN_WIDTH = Globals.SCREEN_WIDTH
SCREEN_HEIGHT = Globals.SCREEN_HEIGHT

screen = Globals.screen
pygame.display.set_caption('Play')

def start(clickDelay = 0.2):
    running = True
    nodes = []

    unassignedNodes = []

    nodeFromSelected = None
    warningButton = Button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.16,70,70,(43,43,55),"")
    screenClickArea = Button.Button(0,SCREEN_HEIGHT*0.15,SCREEN_WIDTH*0.85,SCREEN_HEIGHT*0.85,(43,43,55))
    resetButton = Button.Button(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.5 + (95 * 2),90,90,(35, 35, 38),"Reset")
    modeButton = Button.Button(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.5 + 95,90,90,(35, 35, 38),"Mode: Add")
    runButton = Button.Button(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.5,90,90,(35, 35, 38),"Run")
    backButton = Button.Button((SCREEN_WIDTH - 70) * 0.97,(SCREEN_HEIGHT - 70) * 0.9,70,70,(81,81,88),"Back")
    mode = "ADD"

    pageClickDelay = Delay.Timer(clickDelay)
    pageClickDelay.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False,False
            
        pageClickDelay.update()
        canClickPage = pageClickDelay.timeRanOut

        screen.fill((43,43,55))

        if screenClickArea.drawButton(screen) and canClickPage:
            nodeFromSelected,unassignedNodes = manageScreenClick(nodes,nodeFromSelected,mode,unassignedNodes)
            print(unassignedNodes)
        
        for node in nodes:
            node.drawEdges()

        for node in nodes:
            node.drawNode(screen)

        if resetButton.drawButton(screen) and canClickPage:
            nodes = []
            unassignedNodes = []

        if modeButton.drawButton(screen) and canClickPage:
            if mode == "ADD":
                modeButton.changeText("Mode: Del")
                mode = "DEL"
            else:
                modeButton.changeText("Mode: Add")
                mode = "ADD"
        
        if runButton.drawButton(screen) and canClickPage:
            if len(nodes) > 0:
                if hasCycles(nodes):
                    warningButton.changeText("graph contains cycles therefore tree opperation cannot be performed")
                else:
                    warningButton.changeText("")
                    DFS.DFS(nodes[0])

        warningButton.drawButton(screen,(255,0,0))

        pygame.draw.rect(screen,(35, 35, 38),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT*0.15))

        if backButton.drawButton(screen):
            running = False

        pygame.display.flip() 

    return True,False
    

def manageScreenClick(nodes,nodeFromSelected,mode,unassigned):
    coords = pygame.mouse.get_pos()
    x = coords[0] - 50
    y = coords[1] - 50
    canPlace = True
    alreadyDeleting = False
    for node in nodes:
        if (x - 100 < node.x < x + 100) and (y - 100 < node.y < y + 100) and mode == "ADD":
            canPlace = False
            if nodeFromSelected == None:
                nodeFromSelected = node
            elif nodeFromSelected != node:
                # draw connection 
                nodeFromSelected.addEdge(screen,node)
                nodeFromSelected = None
            break
        else:
            if mode == "DEL" and ((x - 100 < node.x < x + 100) and (y - 100 < node.y < y + 100)) and not alreadyDeleting:
                alreadyDeleting = True
                target = (node.x,node.y)
                unassigned.append(node.id)
                nodes.remove(node)
                dereferenceNode(nodes,node)
                cleanup(nodes,target)
  
    if canPlace and mode == "ADD":
        nodeFromSelected = None
        nodeNum = len(nodes) + 1
        newNode = None
        if len(unassigned) >= 1:
            newNode = GraphClasses.VertexGeometry(unassigned[0],x,y)
            unassigned.remove(unassigned[0])
        else: 
            newNode = GraphClasses.VertexGeometry(len(nodes) + 1,x,y)
        nodes.append(newNode)

    return nodeFromSelected,unassigned

def cleanup(nodes,target):
    for node in nodes:
        for i in node.edges:
            xToo = i.xyToo[0] - 50
            yToo = i.xyToo[1] - 50
            if (xToo,yToo) == target:
                node.edges.remove(i)

def dereferenceNode(nodes,target):
    for node in nodes:
        for connection in node.connections:
            if connection == target:
                node.connections.remove(target)


def hasCycles(nodes):
    incomingEdges = [] + [0] * len(nodes) # array of length len(nodes) that corresponds that has amount of incoming edges for each node
    for node in nodes:
        nodesConnections = node.connections
        for connection in nodesConnections:
            incomingEdges[nodes.index(connection)] = incomingEdges[nodes.index(connection)] + 1
            if incomingEdges[nodes.index(connection)] > 1:
                return True
    return False
