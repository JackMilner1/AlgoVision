# importing the sys module
import sys         
 
# appending the directory of mod.py 
# in the sys.path list
sys.path.append('C:\\Users\\jacke\\Documents\\GitHub\\AlgoVision\\QueueTypes')   
import PriorityQueue # type: ignore

def DijkstrasAlgorithm(graph,start,finish):
    currentVertex = start
    priorityQueue = PriorityQueue.PriorityQueue()
    priorityQueue.enqueue(2)

DijkstrasAlgorithm("1",3,4)
