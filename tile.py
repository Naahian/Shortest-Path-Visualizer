import pygame
from constants import Colors


class Tile:
    def __init__(self, width, row, col, grid):
        self.width = width
        self.grid = grid
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.inverted = False
        self.color = Colors.white
        self.neighbors = []

    def generateNeighbors(self):
        j = self.col
        i = self.row
        
        if(not self.isObstacle()):
            if(not self.grid[i-1][j].isObstacle()):
                self.neighbors.append(self.grid[i-1][j])
            if(not self.grid[i+1][j].isObstacle()):
                self.neighbors.append(self.grid[i+1][j])
            if(not self.grid[i][j-1].isObstacle()):
                self.neighbors.append(self.grid[i][j-1])
            if(not self.grid[i][j+1].isObstacle()):
                self.neighbors.append(self.grid[i][j+1])

    def invertColors(self):
        self.inverted = not self.inverted
        if (self.inverted):
            self.color = Colors.black
        else:
            self.color = Colors.white

    def makeObstacle(self):
        if (self.inverted):
            self.color = Colors.white
        else:
            self.color = Colors.black

    def makeStart(self):
        self.color = Colors.green
        return self.row, self.col

    def makeEnd(self):
        self.color = Colors.red
        return self.row, self.col

    def makePath(self):
        self.color = Colors.blue

    def makeVisited(self):
        self.color = Colors.yellow

    def reset(self):
        self.color = Colors.white

    def isPath(self):
        return self.color == Colors.blue

    def isVisited(self):
        return self.color == Colors.grey

    def isObstacle(self):
        return self.color == Colors.black

    def isStart(self):
        return self.color == Colors.green

    def isEnd(self):
        return self.color == Colors.red

    def isBlank(self):
        return (self.color == Colors.white or 
                self.color == Colors.yellow or
                self.color == Colors.blue)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.width))
