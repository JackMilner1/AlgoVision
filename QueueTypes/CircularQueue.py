class CircularQueue:
    def __init__(self,size,queue=[]):
        self.queue = queue
        self.size = size

        if len(queue) > 0:
            self.front = 0
            self.back = len(queue) - 1
        else:  
            self.front = -1
            self.back = -1

        for i in range(size - len(queue)):
            self.queue.append(None)

    def enqueue(self,item):
        if not self.isFull():
            if self.front == -1 and self.back == -1:
                self.front = 0
                self.back = 0
            
            if not self.isEmpty():
                self.back = (self.back + 1) % self.size
            else:
                print("not inc pointer")

            self.queue[self.back] = item
        else:
            print("queue is full right now")

        return None

    def dequeue(self):

        if self.front == self.back:
            if self.queue[self.front] != None:
                itemToRemove = self.queue[self.front]
                self.queue[self.front] = None
                return itemToRemove
            
            print("queue is currently empty")
        else:
            itemToRemove = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return itemToRemove
        
        return None

    def isFull(self):
        return not (None in self.queue)
    
    def isEmpty(self):
        emptyQueue = []
        for i in range(self.size):
            emptyQueue.append(None)
        
        return self.queue == emptyQueue
    
    def __str__(self):
        return f"Queue: {self.queue}\n\nfront of queue: {self.front}\nback of queue: {self.back}\n"
    

newQueue = CircularQueue(4,[])
print([])
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(5)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(8)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(9)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(12)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(1)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(18)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(9)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(7)
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.dequeue()
print(str(newQueue))
print("-------------------------------------------------")
newQueue.enqueue(9)
print(str(newQueue))
print("-------------------------------------------------")