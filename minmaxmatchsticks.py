# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:18:50 2022

@author: Vedran
"""

class game:
        
    def __init__(self):
        self.stanje = 11
        self.igraPrvi = True
        
    def __str__(self):
        red = ""
        if self.igraPrvi == True:
            red = "P1"
        else:
            red = "P2"
            
        return "Broj Štapića: "+str(self.stanje)+" || Na Redu: "+red
        
    def all_moves(self):        
        moves = []
        
        if self.stanje>1:
            moves.append(2)
            moves.append(1)
        elif self.stanje == 1:
            moves.append(1)
        
        return moves
    
    def move(self, akcija):
        self.stanje = self.stanje - akcija        
        self.igraPrvi = not self.igraPrvi
        
    def undo(self, akcija):
        self.stanje = self.stanje + akcija        
        self.igraPrvi = not self.igraPrvi
        
    def pobjednik(self):
        if self.igraPrvi == True:
            return "P2"        
        else:
            return "P1"        
        
    def game_over(self):
        if self.stanje<2:
            return True
        else:
            return False       
        
counter = 0

def minimax(igra, mo):
    global counter
    counter += 1
    if igra.game_over() == True:
        if igra.pobjednik() == "P2":
            return 100, mo
        elif igra.pobjednik() == "P1":
            return -100, mo
        else:
            return 0, mo
    if igra.igraPrvi == False:
        maxv = -1000
        for m in igra.all_moves():
            igra.move(m)
            v, mm = minimax(igra, m)
            igra.undo(m)
            if v > maxv:
                maxv = v
                maxm = m
        return maxv, maxm
    else:
        minv = 1000
        for m in igra.all_moves():
            igra.move(m)
            v, mm = minimax(igra, m)
            igra.undo(m)
            if v < minv:
                minv = v
                minm = m
        return minv, minm
   
def play():
    while game.game_over() == False:
        print(game.__str__())    
        try:
            unos =  int(input("Da li povlačite jednu ili dvije: "))
        except Exception:
            unos = ""   
        
        if(unos == 2 or unos == 1):
            if unos == 2:
                game.move(2)
            else:
                game.move(1)
                
            if game.game_over():
                print("Pobjednik: "+game.pobjednik())
            else:            
                i, m = minimax(game, 0)
                game.move(m)
                
                if game.game_over():
                    print("Pobjednik: "+game.pobjednik())
        
def perft(igra):
    if igra.game_over() == True:
        return 1
    cnt = 1
    for m in igra.all_moves():
        igra.move(m)
        cnt += perft(igra)
        igra.undo(m)
    return cnt

def minimax_ab(igra, alpha, beta):
    global counter
    counter += 1
    
    if igra.game_over() == True:
        if igra.pobjednik == "P1":
            return 100
        elif igra.pobjednik == "P2":
            return -100
        else:
            return 0
        
    if igra.igraPrvi == False:
        for m in igra.all_moves():
            igra.move(m)
            v = minimax_ab(igra, alpha, beta)
            igra.undo(m)
            if v > alpha:
                alpha = v
            if alpha >= beta:
                break
        return alpha
    else:
        for m in igra.all_moves():
            igra.move(m)
            v = minimax_ab(igra, alpha, beta)
            igra.undo(m)
            if v < beta:
                beta = v
            if alpha >= beta:
                break
        return beta

def podrezivanje():
    minimax_ab(game, -1000, 1000)
    print("Sa podrezivanjem: ",counter)
    print("Bez podrezivanja: ",perft(game))
    
game = game()
play()






    
    