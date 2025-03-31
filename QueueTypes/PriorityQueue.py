class PriorityQueue:

    def __init__(self,queue = []):
        self.queue = queue
        self.createHeap()
        print(self.queue)

    def heaper(self,indexOfSmallest):
        array = self.queue
        sizeOfHeap = len(self.queue)
        smallest = indexOfSmallest
        leftNode = (indexOfSmallest * 2) + 1
        rightNode = (indexOfSmallest * 2) + 2

        if leftNode < sizeOfHeap and array[leftNode] < array[smallest]:
            smallest = leftNode
        
        if rightNode < sizeOfHeap and array[rightNode] < array[smallest]:
            smallest = rightNode

        if smallest != indexOfSmallest:
            array[indexOfSmallest], array[smallest] = array[smallest],array[indexOfSmallest]
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