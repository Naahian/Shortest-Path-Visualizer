import pygame
from constants import *
from gridmap import GridMap
from menu import Menu
from tile import Tile


class PathFinder:
    def __init__(self):
        self.screen: pygame.Surface
        self.screen_size: tuple
        self.running: bool
        self.clock: pygame.time.Clock

        pygame.init()
        pygame.display.set_caption("Shortest Path Visualizer")
        self.screen_size = Resolution.r800x600
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self._initial()

    def loop(self):
        while self.running:
            self._handleEvents()
            self._draw()
            self._update()
            self.clock.tick(Config.fps)

    def _handleEvents(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.running = False
                if (event.key == pygame.K_c):
                    self._restart()
            
            self.menu.listenBtnEvent(event)

        #mouse events
        pos = pygame.mouse.get_pos()
        row, col = self.get_clicked_pos(pos)
        tile = self.map.grid[row][col]
        
        if (pygame.mouse.get_pressed()[0]):
            if ((not tile.isStart()) and (not tile.isEnd())):
                tile.makeObstacle()

        if (pygame.mouse.get_pressed()[2]):
            tile = self.map.grid[row][col]
        
            if (self.startNode == None and tile.isBlank()):
                tile.makeStart()
                self.startNode = tile
            elif (not (self.startNode == None) and (self.endNode == None) and tile.isBlank()):
                tile.makeEnd()
                self.endNode = tile
            elif(not (self.startNode == None) and not (self.endNode == None) and tile.isBlank()):
                self.startNode.reset()
                self.endNode.reset()
                self.startNode = None
                self.endNode = None
                self.map.clearExplored()

             

    def _draw(self):
        self.screen.fill(Colors.white)
        self.map.draw()
        self.menu.draw(self.screen)
        pygame.display.flip()
    
    def redraw(self):
        pygame.draw.rect(self.screen, Colors.white, (0,0,600,600))
        self.map.draw()
        pygame.display.flip()


    def _update(self):
        pass    

    def _restart(self):
        self._initial()
        pygame.draw.rect(self.screen, Colors.white, (0,0,600,600))
        self.map.draw()
        pygame.display.flip()



    def getGameInitials(self):
        return [
            self.map,
            self.startNode,
            self.endNode,
        ]
    
    def _initial(self):
        self.map: GridMap = GridMap(
            screen=self.screen,
            rows=Config.rows,
            width=self.screen_size[1]
        )

        self.startNode:Tile = None
        self.endNode:Tile = None

        self.menu = Menu(
          self.screen_size, 
            self.getGameInitials, 
            self.redraw, 
            self._restart
        )

    def get_clicked_pos(self, pos):
        tile_width = self.map.width // self.map.rows
        y, x = pos
        row = y // tile_width
        col = x // tile_width
        if (row >= Config.rows):
            row = Config.rows-1
        elif (row < 0):
            row = 0
        if (col >= Config.rows):
            col = Config.rows-1
        elif (col < 0):
            col = 0
        return row, col
