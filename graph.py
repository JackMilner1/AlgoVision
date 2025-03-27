class Graph():
    def __init__(self,width,height):
        self.vertices = []
        self.width = width
        self.height = height
        self.addVertices()

    def addVertices(self):
        for i in range(self.width):
            for j in range(self.height):
                newVertex = Vertex((i * self.width) + j)
                self.vertices = self.vertices + [newVertex]

    def drawUI(self):
        pass

class Vertex():
    def __init__(self,id,isWall = False):
        self.id = id
        self.edges = []
        self.isWall = isWall

    def addEdge(self,whereToo,weight = 1):
        if not self.isWall:
            self.edges.append((self.id,whereToo,weight))

    def removeEdge(self,whereToo,weight = 1):
        if not self.isWall:
            self.edges.remove((self.id,whereToo,weight))

    def drawUI(self):
        pass

