import random
import sys
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision\\QueueTypes')   
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision') 
import Stack # type: ignore

def DFS(startNode):
    visited = []
    stack = Stack.Stack()
    currentNode = startNode
    steps = []

    connections = univisitedConnections(currentNode,visited)
    stack.push(currentNode)

    while not stack.isEmpty():
        currentNode = stack.pop()
        connections = univisitedConnections(currentNode,visited)
        print(currentNode.id)
        steps = steps + [currentNode]

        if connections != []:
            stack.push(currentNode)
            chosenNode = selectRandom(connections)
            stack.push(chosenNode)
            currentNode = chosenNode 
        else:
            if not (currentNode in visited):
                visited = visited + [currentNode]
            
    return True

def univisitedConnections(node,visited):
    canVisit = []

    for connection in node.connections:
        if not (connection in visited):
            canVisit = canVisit + [connection]

    return canVisit

def selectRandom(nodes):
    length = len(nodes) - 1
    nodeIndex = random.randint(0,length) 
    return nodes[nodeIndex]
