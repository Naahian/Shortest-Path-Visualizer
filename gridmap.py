import pygame
from constants import Colors
from tile import Tile


class GridMap:
    def __init__(self, width, rows, screen, inverted=False):
        self.width = width
        self.rows = rows
        self.screen = screen
        self.tileWidth = width // rows
        self.inverted = inverted
        self.grid = []
        # create grid
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                tile = Tile(self.tileWidth, i, j)
                if (self.inverted):
                    tile.invertColors()
                self.grid[i].append(tile)

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

