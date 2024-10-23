import pygame
from algorithoms import Algorithoms
from button import Button
from constants import Colors


class Menu:
    def __init__(self,  screenSize, getGameInitials, reDraw, restart):
      
        self.getGameInitials = getGameInitials
        self.reDraw = reDraw
        self.restart = restart
        self.x, self.y = screenSize[1], 0
        self.width = (screenSize[0] - screenSize[1])
        self.height = screenSize[1]
        self.centerX = self.x + (self.width//2)
        self.pad = 40
        
        self.buttons = [
            Button(self.x, self.y, onClick = lambda: self.algoBtnEvent("bfs"), text ="Run BFS", fill=Colors.orange),
            Button(self.x, self.y, onClick = lambda: self.algoBtnEvent("dfs"), text ="Run DFS", fill=Colors.orange),
            Button(self.x, self.y, onClick = lambda: self.algoBtnEvent("dijkstra"), text ="Run Dijkstra", fill=Colors.orange),
            Button(self.x, self.y, onClick = lambda: self.algoBtnEvent("a*"), text ="Run A*", fill=Colors.orange),
            Button(self.x, self.y, onClick = self.randomBtnEvent, text ="Random Maze"),
            Button(self.x, self.y, onClick = self.restart, text ="Reset"),
            Button(self.x, self.y, onClick = self.randomSize, text ="Random Size")
        ]

    def draw(self, surface):
        #background
        pygame.draw.rect(
            surface=surface,color=Colors.dark,
            rect=(self.x, self.y, self.width, self.height)
        )

        #buttons
        self.column(
            surface= surface,
            x = self.centerX - self.buttons[0].width//2,
            y = (self.y-self.pad),
            margin=30,
            children=self.buttons
        )       

    def column(self, x, y, surface, margin:int, children:list):
        y_pos = y
        for i in range(len(children)):
            y_pos += children[i].height + margin
            children[i].y = y_pos
            children[i].x = x
            children[i].draw(surface)

    def algoBtnEvent(self, type = ""):
        map, start, end = self.getGameInitials()
        if(start==None or end==None): return
        map.clearExplored()
        if(type == ""): return
        elif(type == "bfs"): Algorithoms(self.reDraw,map.grid).bfs(start, end)
        elif(type == "dfs"): Algorithoms(self.reDraw,map.grid).dfs(start, end)
        elif(type == "dijkstra"): Algorithoms(self.reDraw,map.grid).dijkstra(start, end)
        elif(type == "a*"): Algorithoms(self.reDraw,map.grid).a_star(start, end)

    def randomBtnEvent(self):
        self.restart()
        map = self.getGameInitials()[0]
        map.randomMaze()
       
    def randomSize(self):
        map = self.getGameInitials()[0]
        map.randomSize()
        self.restart()
    
        
    def listenBtnEvent(self, event):
        for btn in self.buttons:
            btn.handleEvent(event)