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
        visited = [[0 for i in range(len(self.graph))] for j in range(len(self.graph))]
        parents = [[0 for i in range(len(self.graph))] for j in range(len(self.graph))]
        stack = []
        stack.append(start)
        visited[start.col][start.row] = 1

        while(len(stack)>0):
            tile = stack.pop()
            if(tile==end):break
            
            self._drawExplored(tile)

            for nbr in tile.neighbors:
                y, x = nbr.col, nbr.row
                if(visited[y][x] == 0 and not nbr.isObstacle()):
                    visited[y][x] = 1
                    parents[y][x] = tile
                    stack.append(nbr)
        self._backtrack(parents, start, end)
        self._drawPath(start)

    def bfs(self, start:Tile, end:Tile):
        self.path = []  #clear previous data
        queue = []
        visited = [[0 for i in range(len(self.graph))] for j in range(len(self.graph))]
        parents = [[0 for i in range(len(self.graph))] for j in range(len(self.graph))]
        queue.append(start)
        
        while(len(queue)>0):
            tile = queue.pop(0)
            if(tile == end): break
            self._drawExplored(tile)

            for nbr in tile.neighbors:
                y,x = nbr.col, nbr.row
                if(visited[y][x] == 0 and not nbr.isObstacle()):
                    visited[y][x] = 1
                    parents[y][x] = tile
                    queue.append(nbr)

        self._backtrack(parents, start, end)
        self._drawPath(start)

    #to find shortest path
    def _backtrack(self, parents, start, end):
        while True:
            end = parents[end.col][end.row]
            if(end==0): return
            self.path.append(end)
            if(start==end):break


    def A_star(self):
        pass
