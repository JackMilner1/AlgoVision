import pygame

class Button():
    def __init__(self,x, y,width,height,colour,text=""):
        self.colour = colour
        self.text = text
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.topleft = (x,y)
        self.clicked = False
        self.x = x
        self.y = y

    
    def drawButton(self, screen, colour = (255,255,255)):

        action = False
        # get pos of mouse
        pos = pygame.mouse.get_pos()
        # is hovering over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        
        pygame.draw.rect(screen,(self.colour),self.rect)
        self.draw_text(screen,self.text,colour)
        return action
    
    def draw_text(self,screen, text,colour):
        text_color = colour
        font = pygame.font.Font(None, 24)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def changeText(self,newText):
        self.text = newText