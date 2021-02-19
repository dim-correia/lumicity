# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:30:36 2020

@author: dimdim
"""

class Detector():
    
    def __init__(self, x, y):
        self.detect_humain = False
        self.detect_car = False
        self.loc_x = x
        self.loc_y = y
        
    def get_detect_humain(self):
        return self.detect_humain
    
    def get_detect_car(self):
        return self.detect_car
    
    def set_detect_humain(self, boole):
        self.detect_humain = boole
    
    def set_detect_car(self, boole):
        self.detect_car = boole
        
    
    