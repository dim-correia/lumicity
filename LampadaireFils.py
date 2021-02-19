# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:01:20 2020

@author: dimdim
"""
#importations
import pygame

# la calsse
class LampadaireFils(pygame.sprite.Sprite):
    
    def __init__(self, x, y):      
        #super.__init__()
        self.loc_x = x
        self.loc_y = y
        
