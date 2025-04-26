import sys         
 
# appending the directory of mod.py 
# in the sys.path list
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision\\QueueTypes')   
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision') 
import PriorityQueue # type: ignore
import GraphClasses # type: ignore

def AStar(graph,start,finish):
    priorityQueue = PriorityQueue.PriorityQueue()
    vertices = graph.getVertices()

    currentVertex = vertices[start]
    vertices[start].setCost(0,None)
    priorityQueue.enqueue((start,0))

    while not priorityQueue.isEmpty():

        dequeuedElement = priorityQueue.dequeue()
        currentVertex = vertices[dequeuedElement[0]]
        currentCost = dequeuedElement[1]

        if not currentVertex.visited:
            for edge in currentVertex.getEdges():

                if currentCost + edge[2] < vertices[edge[1]].getCost() and not vertices[edge[1]].isWall:
                    vertices[edge[1]].setCost(currentCost + edge[2],currentVertex)
                    priorityQueue.enqueue((edge[1],currentCost + edge[2]))
                    vertices[edge[1]].visiting = True

        currentVertex.visited = True

    
    if vertices[finish].getCameFrom() == None:
        pass
    else:
        return backtrack(vertices[start], vertices[finish])

def backtrack(start,finish):
    path = []
    currentElement = finish
    while currentElement != start and currentElement != None:
        next = currentElement.getCameFrom()
        currentElement = next
        path = [next] + path

    path.append(finish)

    return path
