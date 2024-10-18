import pygame

class Colors:
    white = (255, 255, 255)
    blue = (25, 25, 255)


class Button:
    def __init__(self, x, y,
                onClick=lambda:None,
                width=140, height=50,
                image:str = None,  
                borderColor=Colors.white,
                fill=Colors.blue,
                text = "Click"):
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
       
        
        if(self.image):
            self.surface.blit(self.image, (0,0))
        else:
            #border
            pygame.draw.rect(self.surface, self.borderColor,
                        (0, 0, self.w, self.h),
                        self.border,
                        self.borderRadius+self.border)
            #background
            pygame.draw.rect(self.surface, self.fill,
                        (self.border, self.border, self.w-self.border*2, self.h-self.border*2),
                        0,
                        self.borderRadius)
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

    
        