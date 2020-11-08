#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:27:17 2020

@author: user
"""

import pygame

from pygame.locals import *

class joueur:
    def __init__(self,x,y):
        self.perso=pygame.image.load("piece_joueur.jpg").convert_alpha()
        fenetre.blit(self.perso,(x,y))
        #self.position=self.perso.get_rect()
        self.position=(x,y)
    
    def monter(self):
        
        if self.position[1]>0:
            self.position=(self.position[0],self.position[1]-5)

    
    def descendre(self):
        if self.position[1]<496:
            self.position=(self.position[0],self.position[1]+5)

def MoveBall(x,y,vitessex,vitessey,bcle):
    global speedx
    global speedy
    global boucle
    global scoreJ1
    global scoreJ2
    if bcle>5:
        nvx=x+vitessex
        nvy=y+vitessey
        if vitessex<0:
            #on s'occupe du joueur 1
            if nvx<48:
                if perso1.position[1]-24<=nvy<=perso1.position[1]+99: #si la balle est au niveau de la barre joueur 1
                    speedx=1
                    nvx=x+speedx
                    boucle=0
                    resultat=(nvx,nvy)
                    return resultat
                else :
                    #ajouter 1 au score du joueur 2 et remmetre la partie a 0
                    scoreJ2+=1
                    print("Score :",scoreJ1,"vs",scoreJ2)
                    speedx=1
                    boucle=0
                    resultat=(490,280)
                    return resultat
            else :
                if nvy<0:
                    speedy=1
                    nvy=y+speedy
                elif nvy>575:
                    speedy=-1
                    nvy=y+speedy
                boucle=0
                resultat=(nvx,nvy)
                return resultat
            
            
        elif vitessex>0:
            #on s'occupe du joueur 2
            if nvx>925:
                
                if perso2.position[1]-24<=nvy<=perso2.position[1]+99: #si la balle est au niveau de la barre joueur 2
                    speedx=-1
                    nvx=x+speedx
                    boucle=0
                    resultat=(nvx,nvy)
                    return resultat
                else :
                    #ajouter 1 au score du joueur 2 et remmetre la partie a 0
                    scoreJ1+=1
                    print("Score :",scoreJ1,"vs",scoreJ2)
                    speedx=-1
                    boucle=0
                    resultat=(490,280)
                    return resultat
            else :
                if nvy<0:
                    speedy=1
                    nvy=y+speedy
                elif nvy>575:
                    speedy=-1
                    nvy=y+speedy
                boucle=0
                resultat=(nvx,nvy)
                return resultat
    else :
        resultat=(x,y)
        return resultat
    
##taille des joueurs :: 23*99
pygame.init()

fenetre=pygame.display.set_mode((1000,600))

fond=pygame.image.load("background_pong.png").convert()
fenetre.blit(fond, (0,0))

perso1=joueur(25,250)

perso2=joueur(950,250)

ball=pygame.image.load("balle_pong.png").convert_alpha()
fenetre.blit(ball,(490,280))

pygame.display.flip()

speedx=1
speedy=1
x=490
y=280
boucle=0
scoreJ1=0
scoreJ2=0

continuer=1
pygame.key.set_repeat(100, 30)
while continuer:
    boucle+=1
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer=0
        elif event.type == KEYDOWN :
            if event.key == K_z :
                perso1.monter()
            if event.key == K_s :
                perso1.descendre()
            if event.key == K_UP :
                perso2.monter()
            if event.key == K_DOWN :
                perso2.descendre()
                
    
    
    #recollage de tous les elements
    positionBalle=MoveBall(x,y,speedx,speedy,boucle)
    x=positionBalle[0]
    y=positionBalle[1]
    
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso1.perso,perso1.position)
    fenetre.blit(perso2.perso,perso2.position)
    fenetre.blit(ball,positionBalle)
    
    #rafraichissement de la fenetre
    pygame.display.flip()
    