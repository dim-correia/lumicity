# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:31:12 2020

@author: dimdim
"""

#importations
#from Detector import Detector
from LampadaireFils import LampadaireFils
import pygame
from Detector import Detector 

# la calsse
class LampadaireMaster(pygame.sprite.Sprite):
    
    def __init__(self, x, y, listeDependant, listeProche):
        #super.__init__()
        self.detector = Detector(x, y)
        self.loc_x = x
        self.loc_y = y
        self.lampadairesFilsDependant = listeDependant
        self.lampadaireMasterProches = listeProche
        
    
    def get_detector(self):
        return self.detector
    
    def set_etat(self):
        if Detector.get_detect_humain():
            self.etat = 2
        elif Detector.get_detect_car():
            self.etat = 1
        else:
            self.etat = 0
    