# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:34:40 2020

@author: dimdim
"""
#importations
import pygame
import time
from Simu import Simu


#initialisation
pygame.init()

#fenetre du jeu
pygame.display.set_caption("simu lumicity")
screen = pygame.display.set_mode((750,670))

#les images
background = pygame.image.load('D:/Documents/lumicity/lumicty/assets/bg.jpg')
background2 = pygame.image.load('D:/Documents/lumicity/lumicty/assets/bg2.jpg')

#charger la simu
# 1 humain en haut à gauche au début 
# on récup les lampadaires
Simu = Simu() 

#run
running = True

#accueil
#background
screen.blit(background2, (0,0))   

"""

#txt et elements
color = (0,128,0)
color2 = (252, 243, 207)
color3 = (0,0,0)
pygame.draw.circle(screen, color2, (160,50), 35)
pygame.draw.circle(screen, color, (160,150), 10)
pygame.draw.circle(screen, color3, (160,250), 10)
police = pygame.font.Font(None,72)
texte = police.render("Lampadaire allumé",True, color2)
screen.blit(texte, (200,50))
texte = police.render("Détecteur activé",True, color)
screen.blit(texte, (200,150))
texte = police.render("Détecteur non activé",True, color3)
screen.blit(texte, (200,250))
"""

#maj écran
pygame.display.flip()

#temps affichage
time.sleep(2)

#boucle d'exécution
while running:
    
    #background
    screen.blit(background, (0,0))   
 
    #on met à jour les variables    
    Simu.maj(screen)
    
    #maj écran
    pygame.display.flip()
    
    # condition de sortie : on ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("tchao")       
    
    # pour pas que ca aille trop vite
    time.sleep(.090)

            