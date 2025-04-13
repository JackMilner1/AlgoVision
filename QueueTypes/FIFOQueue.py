class StandardQueue():
    def __init__(self,queue=[]):
        self.queue = queue
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        itemToRemove = self.queue[0]
        self.queue.pop(0)
        return itemToRemove

    def isEmpty(self):
        return len(self.queue) == 0