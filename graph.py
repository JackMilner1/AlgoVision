class Graph():
    def __init__(self,width,height):
        self.vertices = []
        self.width = width
        self.height = height
        self.addVertices()

    def addVertices(self):
        for i in range(self.height):
            for j in range(self.width):
                index = (i * self.width) + j
                newVertex = Vertex(index)
                if index % self.width > 0:
                    newVertex.addEdge(index - 1)

                if (index + 1) % self.width != 0 :
                    newVertex.addEdge(index + 1)

                if index + self.width <= self.width * self.height - 1:
                    newVertex.addEdge(index + self.width)

                if index - self.width >= 0:
                    newVertex.addEdge(index - self.width)

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
        self.isStartEnd = False

    def addEdge(self,whereToo,weight = 1):
        if not self.isWall:
            self.edges.append((self.id,whereToo,weight))

    def printEdges(self):
        for edge in self.edges:
            print(edge)

    def getEdges(self):
        if self.isWall:
            print("wall")
            return []
        
        return self.edges
    
    def getNeighbours(self):
        if self.isWall:
            print("wall")
            return []
        
        neighbours = []
        for edge in self.edges:
            neighbours = neighbours + [edge[1]]
        return neighbours

    def getID(self):
        return self.id

    def drawUI(self):
        pass

    def convertToWall(self):
        self.isWall = True
    
    def revertWall(self):
        self.isWall = False
            

