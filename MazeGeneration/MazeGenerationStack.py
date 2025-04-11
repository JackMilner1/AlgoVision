import QueueTypes.Stack as Stack
import random

def generateMaze(graph,startIndex):
    stack = Stack.Stack()
    vertices = graph.getVertices()
    currentItem = vertices[startIndex]
    stack.push(currentItem)

    while not stack.isEmpty():
        currentItem.visited = True
        currentItem.isPath = True
        connectedNodes = currentItem.getEdges()
        nonVisitedNodes = []

        for node in connectedNodes:
            canTravel = True
            if not vertices[node[1]].visited:
                for nextNode in vertices[node[1]].getEdges():
                    if vertices[nextNode[1]].visited and vertices[nextNode[1]] != vertices[node[0]]:
                       
                        canTravel = False

                if canTravel:
                    nonVisitedNodes = nonVisitedNodes + [vertices[node[1]]]

        if len(nonVisitedNodes) > 0:
            currentItem = nonVisitedNodes[random.randint(0,len(nonVisitedNodes) - 1)]
            stack.push(currentItem)
        else:
            currentItem = stack.pop()

    convertToCorrectFormat(graph)

def convertToCorrectFormat(graph):
    for i in graph.getVertices():
        i.visited = False
        if i.isPath:
            i.isPath = False
        else:
            i.isWall = True

