# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:56:21 2020

@author: dimdim
"""
#importations
from numpy.random import randint
import pygame

#la classe
class Humain(pygame.sprite.Sprite):
    
    def __init__(self, x, y, direction):
        #super.__init__()
        self.speed = randint(1,20) 
        self.image = pygame.image.load('D:/Documents/lumicity/lumicty/assets/ph.PNG')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.direction = direction
        print(self.rect.x)
        print(self.centerx)
        
    def get_rect_x(self):
        return self.rect.x

    def get_rect_y(self):
        return self.rect.y
    
    def get_center_x(self):
        return self.centerx
    
    def get_center_y(self):
        return self.centery
    
    def get_speed(self):
        return self.speed
    
    def set_rect_x(self, x):
        self.rect.x = x 

    def set_rect_y(self, y):
        self.rect.y = y 
        
    def move(self):
        dire = self.direction
        if dire == 'droite':
            self.set_rect_x(self.get_rect_x() + self.get_speed())
        elif dire == 'gauche':
            self.set_rect_x(self.get_rect_x() - self.get_speed())
        elif dire == 'haut':
            self.set_rect_y(self.get_rect_y() - self.get_speed())
        elif dire == 'bas':
            self.set_rect_y(self.get_rect_y() + self.get_speed())
        else:
            print('y a un pb sur la direction')
            
