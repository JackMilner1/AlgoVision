class Graph():
    def __init__(self,width,height):
        self.vertices = []
        self.width = width
        self.height = height
        self.addVertices()

    def addVertices(self):
        for i in range(self.width):
            for j in range(self.height):
                index = (i * self.width) + j
                newVertex = Vertex(index)
                if index % self.width > 0:
                    newVertex.addEdge(index - 1)

                if index + 1 % self.width != 0:
                    newVertex.addEdge(index + 1)

                if index + (self.width - i) <= self.width * self.height - 1:
                    newVertex.addEdge(index + (self.width - i))

                if index - (self.width - i) >= 0:
                    newVertex.addEdge(index - (self.width - i))

                self.vertices = self.vertices + [newVertex]


    def getVertices(self):
        return self.vertices
    
    def printGraph(self):
        for vertex in self.vertices:
            vertex.printEdges()
    
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

    def printEdges(self):
        for edge in self.edges:
            print(edge)

    def getID(self):
        return self.id

    def drawUI(self):
        pass

    def convertToWall(self):
        self.edges = []
    
    def revertWall(self):
        self.isWall = False
            

newGraph = Graph(5,5)
vertices = newGraph.getVertices()
for vertex in vertices:
    print(vertex.getID())
    vertex.printEdges()