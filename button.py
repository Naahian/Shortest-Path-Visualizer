import pygame
from constants import Colors


class Button:
    #file names as Button type
    bfs = "assets/btn_bfs.png"
    dfs = "assets/btn_dfs.png"
    dijkstra = "assets/btn_dijkstra.png"
    a_star = "assets/btn_astar.png"
    maze = "assets/btn_maze.png"
    restart = "assets/btn_restart.png"

    def __init__(self, screen:pygame.Surface, type:str, center=False, onClick= lambda: ()):
        self.onClick = onClick
        self.center = center
        self.screen = screen
        self.type = type
        self.image = pygame.image.load(type).convert_alpha()
        self.rect = self.image.get_rect()

    
    def clickEvent(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            
            if( pygame.mouse.get_pressed()[0]):
                self.onClick()


    def draw(self, x, y):
        if(self.center): self.rect.center = (x, y)
        else: self.rect.topleft = (x, y)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


        
        

    
