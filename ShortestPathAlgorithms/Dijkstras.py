# importing the sys module
import sys         
 
# appending the directory of mod.py 
# in the sys.path list
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision\\QueueTypes')   
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision') 
import PriorityQueue # type: ignore
import GraphClasses # type: ignore
import random

def DijkstrasAlgorithm(graph,start,finish):
    priorityQueue = PriorityQueue.PriorityQueue()
    vertices = graph.getVertices()

    currentVertex = start
    vertices[start].setCostToVertex(0)
    priorityQueue.enqueue((start,0))
    depth = 0 
    while currentVertex != finish and not priorityQueue.isEmpty() and depth != 10:

        currentVertex = vertices[priorityQueue.dequeue()[0]]

        for edge in currentVertex.getEdges():
            weight = random.randint(0,14)
            priorityQueue.enqueue((edge[1],weight))

        depth = depth + 1
        
    print("iteration done")

        
graph = GraphClasses.Graph(5,5)
DijkstrasAlgorithm(graph,3,4)
