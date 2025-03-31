class PriorityQueue:

    def __init__(self,queue = []):
        self.queue = queue
        self.createHeap()
        print(self.queue)

    def heaper(self,currentSmallest):
        array = self.queue
        sizeOfHeap = len(self.queue)
        smallest = currentSmallest
        leftNode = (currentSmallest * 2) + 1
        rightNode = (currentSmallest * 2) + 2

        if leftNode < sizeOfHeap and array[leftNode][1] < array[smallest][1]:
            smallest = leftNode
        
        if rightNode < sizeOfHeap and array[rightNode][1] < array[smallest][1]:
            smallest = rightNode

        if smallest != currentSmallest:
            array[currentSmallest], array[smallest] = array[smallest],array[currentSmallest]
            self.heaper(smallest)

    def createHeap(self):
        size = len(self.queue)
        startIndex = (size // 2) - 1
        for i in range(startIndex, - 1,-1):
            self.heaper(i)

    def enqueue(self,item):
        self.queue.append(item)
        self.createHeap()
        print(f"{item} has been added new queue: {self.queue}")


    def dequeue(self):
        if len(self.queue) > 0:
            itemToRemove = self.queue[0]
            self.queue.pop(0)
            self.createHeap()
            print(f"{itemToRemove} has been removed new queue: {self.queue}")
            return itemToRemove
        
    def isEmpty(self):
        return len(self.queue) == 0
        