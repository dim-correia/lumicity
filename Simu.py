# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:10:23 2020

@author: dimdim
"""
#importations
import pygame
from numpy import sqrt
from Humain import Humain
from LampadaireMaster import LampadaireMaster
from LampadaireFils import LampadaireFils
from numpy.random import randint

class Simu:
    
    ############# initialisation
    
    def __init__(self):        
       
        ############récupération des lampadaires
        
        fils1 = LampadaireFils(80,95)
        fils2 = LampadaireFils(128,95)
        fils3 = LampadaireFils(225,95)
        fils4 = LampadaireFils(275,95)
        fils5 = LampadaireFils(475,95)
        fils6 = LampadaireFils(525,95)
        fils7 = LampadaireFils(620,95)
        fils8 = LampadaireFils(670,95)
        
        fils_ = LampadaireFils(322,48)
        fils_2 = LampadaireFils(425,48)
        
        fi1 = LampadaireFils(705,388)
        fi2 = LampadaireFils(656,388)
        fi3 = LampadaireFils(559,388)
        fi4 = LampadaireFils(509,388)
        fi5 = LampadaireFils(413,388)
        fi6 = LampadaireFils(364,388)
        fi7 = LampadaireFils(268,388)
        fi8 = LampadaireFils(218,388)
        fi9 = LampadaireFils(121,388)
        fi10 = LampadaireFils(73,388)
        
        m1 =  LampadaireMaster(31,96, [fils1,fils2], [])
        m2 = LampadaireMaster(176,96, [fils1,fils2,fils3,fils4], [])
        m3 =  LampadaireMaster(322,96, [fils3,fils4,fils_], [])
        m4 = LampadaireMaster(426,96, [fils5,fils6, fils_2], [])
        m5 = LampadaireMaster(571,96, [fils5,fils6,fils7,fils8], [])
        m6 = LampadaireMaster(718,96, [fils7,fils8], [])
        
        m12 = LampadaireMaster(753,388, [fi1,fi2], [])        
        m7 = LampadaireMaster(608,388, [fi1,fi2,fi3,fi4], [])
        m8 =LampadaireMaster(462,388, [fi3,fi4,fi5,fi6], [])
        m9 = LampadaireMaster(315,388, [fi5,fi6,fi7,fi8], [])
        m10 = LampadaireMaster(170,388, [fi7,fi8,fi9,fi10], [])
        m11 = LampadaireMaster(23,388, [fi9,fi10], [])
       
        m1.lampadaireMasterProches = [m2]
        m2.lampadaireMasterProches = [m1,m3]
        m3.lampadaireMasterProches = [m2,m4]
        m4.lampadaireMasterProches = [m3,m5]
        m5.lampadaireMasterProches = [m4,m6]
        m6.lampadaireMasterProches = [m5]
        m7.lampadaireMasterProches = [m8,m12]
        m8.lampadaireMasterProches = [m7,m9]
        m9.lampadaireMasterProches = [m8,m10]
        m10.lampadaireMasterProches = [m9,m11]
        m11.lampadaireMasterProches = [m10]
        m12.lampadaireMasterProches = [m7]
        
        # recup master
        self.list_lamp_master = [m1, m2, m3, m4,m5,m6,m12,m7,m8,m9,m10,m11]
        

        
        ############# premières entités
        
        #position de départ premier humain
        pos_depart_humain_x = 0 #a modif
        pos_depart_humain_y = 140 #a modif
        self.liste_humain = [Humain(pos_depart_humain_x, pos_depart_humain_y, 'droite')]
        
        #position éventuelle voiture
        self.liste_car = []
        
        
    ############# les fonctions
    
    def getDistance(self, detect, obj):
        #print(sqrt((detect.loc_x - obj.rect.x)**2 + (detect.loc_y - obj.rect.y)**2))
        #print(sqrt((detect.loc_x - obj.centerx)**2 + (detect.loc_y - obj.centery)**2))
        return sqrt((detect.loc_x - obj.rect.x)**2 + (detect.loc_y - obj.rect.y)**2)
    
    
    
    ############# la mise à jour à chaque instant   
    
    def maj(self, screen):
        
        # creation nvx personne
        if randint(1,500) > 495:
            print('new')
            a = randint(1,5)
            if a == 1:
                x = 0
                y = 140
                direction = 'droite'
            elif a == 2:
                x = 700
                y = 325
                direction = 'gauche'
            elif a == 3:
                x = 700
                y = 140
                direction = 'gauche'
            elif a == 4:
                x = 0
                y = 325
                direction = 'droite'
            self.liste_humain.append(Humain(x,y, direction))
            
        # creation nvlle voitures
        
            
        # deplacement perso
        for perso in self.liste_humain:            
            perso.move()        
            #on elimine ceux qui sortent de l'écran
            if perso.rect.x < 0 or perso.rect.x > 750 or perso.rect.y <0 or perso.rect.y > 500:
                self.liste_humain.remove(perso)
                
        #deplacement voiture
        
         
        # affichage des ttes les personens
        for perso in self.liste_humain:
            screen.blit(perso.image, perso.rect)
            
        # affichage voiture
            
        #boucle sur les lampadaires
        for lampeM in self.list_lamp_master:
            
            # on met à jour les détecteurs dhumain
            distance_detection = 100 # valeue de 5 à vérif
            cond = False
            for perso in self.liste_humain:
                if self.getDistance(lampeM.get_detector(), perso) < distance_detection: 
                    cond =  True # true si humain detectable
                    break
            lampeM.get_detector().set_detect_humain(cond)
            
            # on met à jour les détecteurs de voiture
            distance_detection = 15 # valeue de 15 à vérif
            cond = False
            for voit in self.liste_car:
                if self.getDistance(lampeM.get_detector(), voit) < distance_detection: 
                    cond =  True # true si humain detectable
                    break
            lampeM.get_detector().set_detect_car(cond)
            
            #on voit si on allume ou pas
            color =(0,0,0)
            if lampeM.get_detector().get_detect_humain():
                # on allume fort
                color = (0,128,0)                
                # éclairage
                color2=(252, 243, 207)
                pygame.draw.circle(screen, color2, (lampeM.loc_x, lampeM.loc_y), 35)
                for fils in lampeM.lampadairesFilsDependant:
                    pygame.draw.circle(screen, color2, (fils.loc_x, fils.loc_y), 35)                    
                for proche in lampeM.lampadaireMasterProches:
                    pygame.draw.circle(screen, color2, (proche.loc_x, proche.loc_y), 35)
                    for fils in proche.lampadairesFilsDependant:
                        pygame.draw.circle(screen, color2, (fils.loc_x, fils.loc_y), 35)
        
        for lampeM in self.list_lamp_master:
            #on voit si on allume ou pas
            color =(0,0,0)
            if lampeM.get_detector().get_detect_humain():
                # on allume fort
                color = (0,128,0)   
            # signalement détecteur
            pygame.draw.circle(screen, color, (lampeM.loc_x, lampeM.loc_y), 10)
            
            
            

        

        