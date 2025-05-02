import pygame

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

    def reset(self):
        for vertex in self.vertices:
            vertex.visited = False
            vertex.setCost(10000000000,None)

    def getVertices(self):
        return self.vertices
    
    def getVertex(self,index):
        if index >= 0 and index <= len(self.vertices):
            return self.vertices[index]
    
    def printGraph(self):
        for vertex in self.vertices:
            vertex.printEdges()
    
    def drawUI(self):
        pass

class Vertex():
    def __init__(self,id,isWall = False):
        self.id = id
        self.cost = 10000
        self.edges = []
        self.isWall = isWall
        self.isStartEnd = False
        self.isPath = False
        self.visited = False
        self.visiting = False
        self.cameFrom = None

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

    def convertToWall(self):
        self.isWall = True
    
    def revertWall(self):
        self.isWall = False

    def setCost(self,newVal,cameFrom):
        self.cost = newVal
        self.cameFrom = cameFrom

    def getCameFrom(self):
        return self.cameFrom

    def getCost(self):
        return self.cost
    
    def reset(self):
        self.cost = 10000
        self.isWall = False
        self.isStartEnd = False
        self.isPath = False
        self.visited = False
        self.visiting = False
        self.cameFrom = None

class VertexGeometry(Vertex):
    def __init__(self, id, x, y, isWall=False):
        super().__init__(id, isWall)
        self.x = x
        self.y = y
        self.connections = []

    def drawNode(self,screen):
        x,y = self.x,self.y
        nodeRect = pygame.Rect(x,y,100,100)
        pygame.draw.rect(screen,(0,0,0),nodeRect,border_radius=100)
        pygame.draw.rect(screen,(35, 35, 38),(x + 5,y + 5,90,90),border_radius=100,width=5)
        self.draw_text(screen, str(self.id),nodeRect)

    def drawEdges(self):
        for edge in self.edges:
            edge.drawEdge()
            
    def addEdge(self,screen, node2):
        self.connections = self.connections + [node2]
        newEdge = EdgeGeometry(screen,(0,0,0),(self.x + 50 ,self.y + 50), (node2.x + 50,node2.y + 50),width=10)
        self.edges.append(newEdge)

    def draw_text(self,screen, text, button_rect):
        text_color = (255, 255, 255)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

class EdgeGeometry():
    def __init__(self,screen,colour,xyFrom,xyToo,width = 10):
        self.screen = screen
        self.colour = colour
        self.xyFrom = xyFrom
        self.xyToo = xyToo
        self.width = width
    
    def drawEdge(self):
        pygame.draw.line(self.screen,self.colour,self.xyFrom, self.xyToo,width=10)
    
