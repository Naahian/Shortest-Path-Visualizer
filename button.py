import pygame

from constants import Colors


class Button:
    def __init__(self, x, y,
                onClick=lambda:None,
                width=140, height=50,
                image:str = None,  
                borderColor=Colors.black,
                fill=Colors.blueAccent,
                text = "Click"
                ):
        self.w, self.h = width, height
        self.surface = pygame.surface.Surface((width,height))
        self.surface.set_colorkey((0,0,0))
        self.rect = pygame.Rect(x,y,width, height)
        
        self.borderColor = borderColor
        self.fill = fill
        self.text = text
        self.fontSize = 24
        self.borderRadius = 10
        self.border = 2
        self.onclick = onClick
        self.clicked = False
        self.hovered = False
    
        if(image):
            self.image = pygame.image.load(image).convert()
            self.image = pygame.transform.scale(self.image, (self.w, self.h))
        else: self.image = None
    
    
    
    def draw(self, surface:pygame.Surface):
        #background
        if(self.image):
            self.rect_image = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            self.image = self.image.copy().convert_alpha()
            pygame.draw.rect(self.rect_image, Colors.white,
                        (self.border, self.border, self.w-self.border*2, self.h-self.border*2),
                        0,
                        self.borderRadius)
            self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN )
            self.surface.blit(self.image, (0,0))
        else:
            pygame.draw.rect(self.surface, self.fill,
                        (self.border, self.border, self.w-self.border*2, self.h-self.border*2),
                        0,
                        self.borderRadius)
       #border
        pygame.draw.rect(self.surface, self.borderColor,
                    (0, 0, self.w, self.h),
                    self.border,
                    self.borderRadius+self.border)
        self.drawText()
        surface.blit(self.surface, (self.rect.x, self.rect.y))


    def drawText(self):
        font = pygame.font.SysFont("Ariel", self.fontSize)
        img = font.render(self.text, True, self.borderColor)
        imgW, imgH = img.get_width(), img.get_height()
        centerX, centerY = self.w//2, self.h//2
        x, y = (centerX - imgW//2), (centerY - imgH//2) 
        self.surface.blit(img, (x,y))
    


    def handleEvent(self, event:pygame.event):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if(not self.hovered):
                self.hovered = True
                temp = self.fill
                self.fill = self.borderColor
                self.borderColor = temp
                
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.clicked = True
                self.rect.y += 2
                self.onclick()
    
            if (event.type == pygame.MOUSEBUTTONUP):
                self.clicked = False  
                self.rect.y -= 2

        if(self.hovered and not self.rect.collidepoint(pos)):
            self.hovered = False
            temp = self.borderColor
            self.borderColor = self.fill
            self.fill = temp

    
        