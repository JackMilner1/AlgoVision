import pygame

WALL_COLOUR = (0,0,0)
START_END_COLOUR = (115, 232, 111)

class GridSquare():
    def __init__(self,vertexClass,x, y,width,height, colour):
        self.vertex = vertexClass
        self.colour = colour
        self.selectable = True
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.topleft = (x,y)
        self.clicked = False
        self.moving = False
        self.x = x
        self.y = y

    
    def drawButton(self, screen):
        if not self.selectable:
            return

        action = False
        # get pos of mouse
        pos = pygame.mouse.get_pos()
        # is hovering over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                if not self.vertex.isWall:
                    self.vertex.convertToWall()
                self.vertex.isStartEnd = False
                self.clicked = True
                self.moving = True
                action = True

            if pygame.mouse.get_pressed()[1] == 1 and not self.clicked:
                self.vertex.isStartEnd = True
                self.clicked = True
                self.moving = True
                action = True

            if pygame.mouse.get_pressed()[2] == 1 and not self.clicked:
                if self.vertex.isWall:
                    self.vertex.revertWall()
                self.vertex.isStartEnd = False
                self.clicked = True
                self.moving = True
                action = True


        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.moving = False

        if self.vertex.isWall:
            pygame.draw.rect(screen,(WALL_COLOUR),self.rect)
        elif self.vertex.isStartEnd:
            pygame.draw.rect(screen,(START_END_COLOUR),self.rect)
        else:        
            pygame.draw.rect(screen,(self.colour),self.rect)
        return action
    
    def getClass(self):
        return self.vertex