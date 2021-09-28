# -*- coding: utf-8 -*-
"""
Created in August 2021

@author: chirayu
"""

'''Simulation of Langton's Ant, a type of cellular automata, pygame is used for animation. The rules for the 
game can be found here: https://en.wikipedia.org/wiki/Langton%27s_ant
Note that intead of a white square I have used a red square. '''
import pygame
import time
pixel=2 #Width of each square in coordinate system
black=(0,0,0)
red=(255,0,0)
grid=(500,320)
frame_per_sec=60
gen_per_frame=20 #Adjust thi depending on CPU speed
'''0->right, 1->up, 2->left, 3->down'''
direct={0:[1,0], 1:[0,1], 2:[-1,0], 3:[0,-1]} #Dictionary for direction the ant will movw depending on direction it is facing
class ant():
    def __init__(self):
        print(grid[1]/2)
        self.x=int(grid[0]/2) # Initialise the ant in the middle of the screen
        self.y=int(grid[1]/2)
        self.face=0 # Starts of facing to the right
    
    
    def turn_clockwise(self):
        self.face+=3 
        self.face=self.face%4

        
    
    def turn_anticlockwise(self):

        self.face+=1
        self.face=self.face%4
        
    def move(self):
        self.x+=direct[self.face][0]
        self.y+=direct[self.face][1]
        self.x=self.x % grid[0] #This is to make sure the ant loops and stays on grid
        self.y=self.y % grid[1]
        
def display_screen():
    pygame.init()
    screen=pygame.display.set_mode((grid[0]*pixel,grid[1]*pixel))
    screen.fill(pygame.Color('black'))
    clock=pygame.time.Clock()
    
    return screen, clock
    
def generation(Ant, squares, screen, start):
    if squares[Ant.x][Ant.y]==1: #if coloured
        Ant.turn_clockwise()
        squares[Ant.x][Ant.y]=0
        pygame.draw.rect(screen, black, (Ant.x*pixel, Ant.y*pixel, pixel, pixel))# Making it 'pixel' pixels dimension square
    elif squares[Ant.x][Ant.y]==0:
        Ant.turn_anticlockwise()
        squares[Ant.x][Ant.y]=1
        pygame.draw.rect(screen, red, (Ant.x*pixel, Ant.y*pixel, pixel, pixel))
    Ant.move()
    
def main():
    gen=0
    screen, clock= display_screen()
    pygame.display.set_caption("Langton's Ant")
    start=time.time()
    time.sleep(0.3)
    Ant=ant()
    squares=[[0 for i in range(grid[1])]for j in range(grid[0])]
    run=True
    while run:
        for i in range(gen_per_frame):
            gen+=1
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
            generation(Ant, squares, screen, start)
        
        pygame.display.update()
        pygame.display.set_caption("Langton;s Ant | Generation {0}". format(gen))
        
        clock.tick(frame_per_sec)
        
main()
    
         
        