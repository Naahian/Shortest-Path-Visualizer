from queue import PriorityQueue
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
    
    def _drawPath(self, start):        
        for tile in self.path:
            if(not tile==start): tile.makePath()
            self.draw()
          
    def dfs(self, start:Tile, end:Tile):
        self.path = [] #clear previous data
        visited = {tile:False for row in self.graph for tile in row}
        parents = {tile:None for row in self.graph for tile in row}
        stack = []
        stack.append(start)
        visited[start] = True

        while(len(stack)>0):
            tile = stack.pop()
            if(tile==end):break
            
            self._drawExplored(tile)

            for nbr in tile.neighbors:
                if(not visited[nbr] and not nbr.isObstacle()):
                    visited[nbr] = True
                    parents[nbr] = tile
                    stack.append(nbr)
        self._backtrack(parents, start, end)
        self._drawPath(start)

    def bfs(self, start:Tile, end:Tile):
        self.path = []  #clear previous data
        queue = []
        visited = {tile:False for row in self.graph for tile in row}
        parents = {tile:None for row in self.graph for tile in row}
        queue.append(start)
        visited[start] = True
        
        while(len(queue)>0):
            tile = queue.pop(0)
            if(tile == end): break
            self._drawExplored(tile)

            for nbr in tile.neighbors:
                if(not visited[nbr] and not nbr.isObstacle()):
                    visited[nbr] = True
                    parents[nbr] = tile
                    queue.append(nbr)

        self._backtrack(parents, start, end) 
        self._drawPath(start)

    #output same as bfs since undirected graph
    def dijkstra(self ,start:Tile, end:Tile):
        self.path = []  #clear previous data
        queue = []
        parents = {tile:None for row in self.graph for tile in row}
        distance = [[float('inf') for i in range(len(self.graph))] for j in range(len(self.graph))]
        queue.append(start)
        distance[start.col][start.row] = 0

        while(len(queue)>0):
            tile = queue.pop(0)
            if(tile == end): break
            self._drawExplored(tile)

            for nbr in tile.neighbors:
                y,x = nbr.col, nbr.row
                ty, tx = tile.col, tile.row
                tempDist = distance[ty][tx] + 1

                if(tempDist < distance[y][x] and not nbr.isObstacle()):
                    distance[y][x] = tempDist
                    parents[nbr] = tile
                    queue.append(nbr)

        self._backtrack(parents, start, end)
        self._drawPath(start)



    def a_star(self, start:Tile, end:Tile):
        self.path = []  #clear previous data
        pqueue = [] 
        g_score = {tile:float('inf') for row in self.graph for tile in row}
        f_score = {tile:float('inf') for row in self.graph for tile in row}
        visited = {tile:False for row in self.graph for tile in row}
        parents = {tile:None for row in self.graph for tile in row}

        pqueue.append((f_score[start], start)) #(f_score, tile)
        visited[start] = True
        g_score[start] = 0
        f_score[start] = self.h_score(start, end)

        while(len(pqueue) > 0):
            tileData = self.pop_min(pqueue, 0)
            tile = tileData[1]
            self._drawExplored(tile)            
            if(tile == end): break

            for nbr in tile.neighbors:
                if(not visited[nbr] and not nbr.isObstacle()):
                    visited[nbr] = True
                    parents[nbr] = tile
                    g_score[nbr] = g_score[tile] + 1
                    h = self.h_score(nbr, end)
                    f_score[nbr] = g_score[nbr] + h
                    pqueue.append((f_score[nbr], nbr))
        
        self._backtrack(parents, start, end)
        self._drawPath(start)



    def pop_min(self, queue:list, index):
        min = queue[0]
        for item in queue:
            if(item[index] < min[index]): min = item
        queue.remove(min)
        return min
    
    #heuristic
    def h_score(self, current:Tile, end:Tile):
        return abs((current.row - end.row)) + abs((current.col - end.col))

    #to find shortest path
    def _backtrack(self, parents, start, end):
        while True:
            end = parents[end]
            if(end==None): return
            self.path.append(end)
            if(start==end):break
