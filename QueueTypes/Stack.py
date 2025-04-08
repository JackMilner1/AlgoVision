
class Stack():
    def __init__(self,size = 11):
        self.stackArray = []
        self.size = size

    def pop(self):
        if not self.isEmpty():
            return self.stackArray.pop(0)

    def push(self,item):
        self.stackArray = [item] + self.stackArray

    def isEmpty(self):
        return len(self.stackArray) == 0

    def getElements(self):
        return self.stackArray
    
    def maxItems(self):
        return self.size
    
    def howManyItems(self):
        return len(self.stackArray)

    def clear(self):
        self.stackArray = []
