# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:18:50 2022

@author: Vedran
"""
import random

class game:
        
    def __init__(self):
        self.stanje = 11
        self.igraPrvi = True
        self.zadnjiDvi = "Nitko"
        
    def __str__(self):
        red = ""
        if self.igraPrvi == True:
            red = "P1"
        else:
            red = "P2"
            
        return "Broj Štapića: "+str(self.stanje)+" || Na Redu: "+red+" || Zadnji povukao 2: "+self.zadnjiDvi
        
    def all_moves(self):        
        moves = []
        
        if self.stanje>1:
            moves.append(2)
            moves.append(1)
        elif self.stanje == 1:
            moves.append(1)
        else:
            moves = []
        
        return moves
    
    def move(self, igrac, akcija):
        self.stanje = self.stanje - akcija
        if akcija == 2:
            if self.igraPrvi == True:
                self.zadnjiDvi = "P1"
            else:
                self.zadnjiDvi = "P2"
        self.igraPrvi = not self.igraPrvi
        
    def game_over(self):
        if self.stanje<2:
            return True
        else:
            return False       
   
        
game = game()

while game.game_over() == False:
    print(game.__str__())
    unos =  int(input("Da li povlačite jednu ili dvije"))
    
    if(unos == 2 or unos == 1):
        if unos == 2:
            game.move(game.igraPrvi, 2)
        else:
            game.move(game.igraPrvi, 1)
            
        if game.game_over():
            print("Pobjednik: "+game.zadnjiDvi)
        else:            
            i = random.randint(1,2)
            game.move(game.igraPrvi, i)
            if game.game_over():
                print("Pobjednik: "+game.zadnjiDvi)
        
        
        
        
    
    
        
    
    