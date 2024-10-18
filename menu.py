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
            Button(self.x, self.y, self.bfsBtnEvent, text="Run BFS"),
            Button(self.x, self.y, self.dfsBtnEvent, text="Run DFS"),
            Button(self.x, self.y, lambda: print("dijkstra"), text="Run Dijkstra"),
            Button(self.x, self.y, lambda: print("A*"), text="Run A*"),
            Button(self.x, self.y, self.randomBtnEvent, text="Random Maze"),
            Button(self.x, self.y, self.restart, text="Restart", image="assets/orangeBtn.png", borderColor=(0,0,0), fill=(255,255,255))
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
            x = self.centerX - self.buttons[0].w//2,
            y = (self.y+self.pad),
            margin=30,
            children=self.buttons
        )       

    def column(self, x, y, surface, margin:int, children:list):
        y_pos = y
        for i in range(len(children)):
            y_pos = children[i].rect.height*(i) + margin*(i+2)
            children[i].rect.y = y_pos
            children[i].rect.x = x
            children[i].draw(surface)

    def bfsBtnEvent(self):
        map, start, end = self.getGameInitials()
        if(start==None or end==None): return
        map.clearExplored()
        Algorithoms(self.reDraw,map.grid).bfs(start, end)
    
    def dfsBtnEvent(self):
        map, start, end = self.getGameInitials()
        map.clearExplored()
        if(start==None or end==None): return
        Algorithoms(self.reDraw,map.grid).dfs(start, end)

    def randomBtnEvent(self):
        self.restart()
        map = self.getGameInitials()[0]
        map.randomMaze()
    
        
    def listenBtnEvent(self, event):
        for btn in self.buttons:
            btn.handleEvent(event)