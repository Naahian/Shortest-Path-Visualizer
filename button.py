import pygame
from constants import Colors


class Button:
    def __init__(self, x, y,
                onClick=lambda:None,
                width=140, height=50,
                image:str = None,  
                borderColor=Colors.white,
                fill=Colors.blueAccent,
                text = "Click",
                centered = False,
                borderRadius = 10
            ):
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.surface = pygame.surface.Surface((width,height))
        self.surface.set_colorkey((0,0,0))
        if(centered): self.rect = pygame.Rect(x - width//2, y - height//2,width, height)
        else: self.rect = pygame.Rect(x,y,width, height)
        self.borderColor = borderColor
        self.fill = fill
        self.text = text
        self.fontSize = 24
        self.borderRadius = borderRadius
        self.border = 2
        self.onclick = onClick
        self.clicked = False
        self.hovered = False
        if(image):
            self.image = pygame.image.load(image).convert()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else: self.image = None
    
    
    
    def draw(self, surface:pygame.Surface):
        self.rect.x, self.rect.y = self.x, self.y
        #background
        if(self.image):
            self.rect_image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            self.image = self.image.copy().convert_alpha()
            pygame.draw.rect(self.rect_image, Colors.white,
                        (0, 0, self.width, self.height),
                        0,
                        self.borderRadius)
            self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN )
            self.surface.blit(self.image, (0,0))
        else:
            pygame.draw.rect(self.surface, self.fill,
                        (0, 0, self.width, self.height),
                        0,
                        self.borderRadius)
       
       #border
        if(self.hovered):
            pygame.draw.rect(self.surface, self.borderColor,
                        (0, 0, self.width, self.height),
                        self.border,
                        self.borderRadius+self.border)
        self.drawText()
        surface.blit(self.surface, (self.x,self.y))


    def drawText(self):
        font = pygame.font.SysFont("Ariel", self.fontSize)
        img = font.render(self.text, True, self.borderColor)
        imgW, imgH = img.get_width(), img.get_height()
        centerX, centerY = self.width//2, self.height//2
        x, y = (centerX - imgW//2), (centerY - imgH//2) 
        self.surface.blit(img, (x,y))
    


    def handleEvent(self, event:pygame.event):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if(not self.hovered):
                self.hovered = True
                self.border = 2
                
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.clicked = True
                temp = self.fill
                self.fill = self.borderColor
                self.borderColor = temp
                
    
            if (event.type == pygame.MOUSEBUTTONUP):
                self.clicked = False  
                temp = self.borderColor
                self.borderColor = self.fill
                self.fill = temp
                self.onclick()

        if(self.hovered and not self.rect.collidepoint(pos)):
            self.hovered = False
            self.border = 0

    
        