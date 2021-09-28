# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:32:34 2021

@author: chi20
"""
'''This is a simulation of Conways Game of Life (A cellular automata). The rules for the game can be found 
on Wikipedia: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life'''
import pygame
import random
import time

pop=400 # Initial population
grid=(150,80)
pixel=8 # Width of each cell
white=(0,255,0)
black=(0,0,0)
frame_per_sec=10
gen_per_frame=1

def display_screen():
    pygame.init()
    screen=pygame.display.set_mode((grid[0]*pixel,grid[1]*pixel))
    screen.fill(pygame.Color('black'))
    clock=pygame.time.Clock()
    
    return screen, clock


def check_neighbours(squares, i, j):
    tot=0
    
    if squares[i][j+1]==1:
        tot+=1
    if squares[i+1][j]==1:
        tot+=1
    if squares[i][j-1]==1:
        tot+=1
    if squares[i-1][j]==1:
        tot+=1
    if squares[i+1][j+1]==1:
        tot+=1
    if squares[i-1][j-1]==1:
        tot+=1
    if squares[i+1][j-1]==1:
        tot+=1
    if squares[i-1][j+1]==1:
        tot+=1
    return tot


def initial(pop, squares):
    '''Makes the initial grid with a random population distribution'''
    for i in range(pop):
    
        x=random.randint(int(0.3*grid[0]), int(0.7*grid[0]))
        y=random.randint(int(0.3*grid[1]), int(0.7*grid[1]))
        squares[x][y]=1
    return squares
    
    
    
    
def generation(squares, screen):
    squares_new=[[0 for i in range(grid[1])] for j in range(grid[0])]
    for i in range(1, grid[0]-1):
        for j in range(1, grid[1]-1):
            Alive=squares[i][j]
            neighbours=check_neighbours(squares, i, j)
            if Alive==1:
                
                if neighbours<2 or neighbours>3: #dies of overpopulation or underpopulation
                    
                    squares_new[i][j]=0#dies
                else:
                    squares_new[i][j]=1 #stays alive'''
            else:
                if neighbours==3:
                    squares_new[i][j]=1 #becomes alive
                    
                else:
                    squares_new[i][j]=0#stays dead
 
    return squares_new

def draw(squares, screen):
    for i in range(grid[0]):
        for j in range(grid[1]):
            if squares[i][j]==1:
                pygame.draw.rect(screen, white, (i*pixel, j*pixel, pixel, pixel))
            elif squares[i][j]==0:
                pygame.draw.rect(screen, black, (i*pixel, j*pixel, pixel, pixel))
        
                

             
def main():
    screen, clock= display_screen()
    pygame.display.set_caption("Conway's Game Of Life")
    time.sleep(0.1)
    
    squares=[[0 for i in range(grid[1])]for j in range(grid[0])]
    squares=initial(pop, squares)
    draw(squares, screen)
    pygame.display.update()
    time.sleep(0.5) #To see initial coniguration
    run=True
    gen=0
    while run:
        for i in range(gen_per_frame):
            gen+=1
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
            squares=generation(squares, screen)
            draw(squares, screen)
        pygame.display.update()
        pygame.display.set_caption("Conway's Game of Life| Generation {0}".format(gen))
        
        clock.tick(frame_per_sec)
        
main()
                    
                    
                    
                    
                    
                
            
    
        
            
        
    
    

