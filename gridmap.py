import pygame
from constants import Colors
from tile import Tile


class GridMap:
    def __init__(self, width, rows, screen, ):
        self.width = width
        self.rows = rows
        self.screen = screen
        self.tileWidth = width // rows
        
        self.grid = []
        self._createGrid()
        self._createNeighbors()

    def _createGrid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                tile = Tile(self.tileWidth, i, j, self.grid)
                if(i==0 or j==0 or i==(self.rows-1) or j==(self.rows-1)): #make boundary barier
                    tile.makeObstacle() 
                self.grid[i].append(tile)
        
    
    def _createNeighbors(self):
        for row in self.grid:
            for tile in row:
                tile.generateNeighbors()

    def _drawTiles(self):
        for row in self.grid:
            for tile in row:
                tile.draw(self.screen)
                

    def _drawGrid(self):
        for i in range(self.rows):
            pygame.draw.line(self.screen, Colors.grey, (0, i *
                             self.tileWidth), (self.width, i*self.tileWidth))
            pygame.draw.line(self.screen, Colors.grey,
                             (i*self.tileWidth, 0), (i*self.tileWidth, self.width))

    def draw(self):
        self._drawTiles()
        self._drawGrid()

