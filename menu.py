import pygame
from algorithoms import Algorithoms
from button import Button
from constants import Colors



class Menu:
    def __init__(self, screen, screenSize, getGameInitials, reDraw, restart):
        self.screen = screen
        self.getGameInitials = getGameInitials
        self.reDraw = reDraw
        self.restart = restart
        self.x, self.y = screenSize[1], 0
        self.width = (screenSize[0] - screenSize[1])
        self.height = screenSize[1]
        self.centerX = self.x + (self.width//2)
        self.pad = 40
        
        self.buttons = [
            Button(self.screen,Button.bfs,True, self.bfsBtnEvent),
            Button(self.screen,Button.dfs,True, self.dfsBtnEvent),
            Button(self.screen,Button.dijkstra,True, lambda: print("dijkstra")),
            Button(self.screen,Button.a_star,True, lambda: print("A*")),
            Button(self.screen,Button.maze,True, self.randomBtnEvent),
            Button(self.screen,Button.restart,True, self.restart)
        ]

    def draw(self):
        #background
        pygame.draw.rect(
            surface=self.screen,color=Colors.dark,
            rect=(self.x, self.y, self.width, self.height)
        )

        #buttons
        self.column(
            x = self.centerX,
            y = (self.y+self.pad),
            gap=30,
            children=self.buttons
        )       

    def column(self, x, y, gap:int, children:list):
        y_pos = y
        for i in range(len(children)):
            y_pos = children[i].rect.height*(i) + gap*(i+2)
            children[i].draw(x, y_pos)

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
    
        
    def listenBtnEvent(self):
        for btn in self.buttons:
            btn.clickEvent()