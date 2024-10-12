import pygame
from tile import Tile


class Algorithoms:
    def __init__(self, draw, tileList:list):
        self.path = []
        self.graph:list = tileList
        self.draw = draw 

    def _drawExplored(self, tile):
        if((not tile.isStart()) and (not tile.isEnd())):
            tile.makeVisited()
            self.draw()

    def _drawPath(self):
        for tile in self.path:
            if((not tile.isStart()) and (not tile.isEnd())):
                tile.makePath()
                self.draw()


    def dfs(self):
        stack = []

    #since weight is 1 for all vertices
    def bfs_dijkstra(self, start:Tile, end:Tile):
        queue = []
        visited = [[0 for i in range(len(self.graph))] for j in range(len(self.graph))]
        parents = [[0 for i in range(len(self.graph))] for j in range(len(self.graph))]
        queue.append(start)
        
        while(len(queue)>0):
            tile = queue.pop(0)
            if(tile == end): break

            for nbr in tile.neighbors:
                self._drawExplored(tile)
                y,x = nbr.col, nbr.row
                if(visited[y][x] ==0 and not nbr.isObstacle()):
                    visited[y][x] = 1
                    parents[y][x] = tile
                    queue.append(nbr)

        self.makePath(parents, start, end)
                    
    def makePath(self, parents, start, end):
        while True:
            end = parents[end.col][end.row]
            self.path.append(end)
            if(start==end):break

        for tile in self.path:
            if(not tile==start): tile.makePath()
        self.draw()
          

    def A_star(self):
        pass
