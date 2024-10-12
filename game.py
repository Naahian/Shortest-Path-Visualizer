import pygame
from algorithoms import Algorithoms
from constants import *
from gridmap import GridMap


class AlgoVisualizer:
    def __init__(self):
        self.screen: pygame.Surface
        self.screen_size: tuple
        self.running: bool
        self.clock: pygame.time.Clock

        pygame.init()
        pygame.display.set_caption("Shortest Path Visualizer")
        self.screen_size = Resolution.r600x600
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
                if (event.key == pygame.K_r):
                    self._restart()
                if (event.key == pygame.K_i):
                    self._restart(inverted = not self.map.inverted)
                #start algo
                if (event.key == pygame.K_SPACE):
                    for i in range(Config.rows):
                        for j in range(Config.rows):
                            if(i==j):
                                self.map.grid[i][j].makeEnd()
                                pygame.time.delay(30)
                                self._draw()
    def _draw(self):
        self.screen.fill(Colors.white)
        self.map.draw()
        pygame.display.flip()

    def _update(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_clicked_pos(pos)
        tile = self.map.grid[row][col]

        if (pygame.mouse.get_pressed()[0]):
            if ((not tile.isStart()) and (not tile.isEnd())):
                tile.makeObstacle()
        if (pygame.mouse.get_pressed()[2]):
            tile = self.map.grid[row][col]
        
            if (not self.hasStart and tile.isBlank()):
                tile.makeStart()
                self.hasStart = True
            elif (self.hasStart and not self.hasEnd and tile.isBlank()):
                tile.makeEnd()
                self.hasEnd = True
        

    def _restart(self, inverted=False):
        self._initial(inverted=inverted)
        self._draw()

    def _initial(self, inverted=False):
        self.map: GridMap = GridMap(
            screen=self.screen, rows=Config.rows, width=self.screen_size[0], inverted=inverted)
        
        self.hasStart = False
        self.hasEnd = False

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
