from gridmap import GridMap


class Algorithoms:
    def __init__(self, tileList:list):
        self.path = []
        self.graph = tileList
        print(self.graph)
         
    def dfs(self):
        stack = []

    #since weight is 1 for all vertices
    def bfs_dijkstra(self):
        queue = []
        queue.append(self.graph[0])
        while(len(queue)>0):
            v = queue.pop(0)
            self.path.append(v)
            for nbr in v:
                queue.append(nbr)
                #TODO:color the tile since explored
        #TODO: color the path
        print(self.path)

    def A_star(self):
        pass
