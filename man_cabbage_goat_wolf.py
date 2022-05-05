# -*- coding: utf-8 -*-
"""
Created on Mon Apr  25 21:04:36 2022

@author: Vedran
"""

import copy as copy

class stanje():
    
    dic = {
        "man": "",
        "cabbage": "",
        "goat": "",
        "wolf": ""
        }
    
    done = []
    
    def __init__(self):
        self.dic["man"] = "A"
        self.dic["cabbage"] = "A"
        self.dic["goat"] = "A"
        self.dic["wolf"] = "A"
        
    def as_string(self):
        s = ""
        for x in self.dic:
            s += x
            s += ": "
            s += self.dic[x]
            s += " "        
        return s     
        
    def all_actions(self, st):
        
        akcije = []
        covjek = {}
        
        if st["man"] == "A":
            lokacija = "A"
            suprotno = "B"
            covjek["man"] = suprotno
            akcije.append(covjek)
        else:
            lokacija = "B"
            suprotno = "A"
            covjek["man"] = suprotno
            akcije.append(covjek)
        
        for x in st:
            akcija = {}
            if st[x] == lokacija and x != "man":
                akcija[x] = suprotno
                akcija["man"] = suprotno
                akcije.append(akcija)             
                
        return akcije        
    
    def next_states(self, st):
        
        stanja = []        
        akc = self.all_actions(st)
        
        for x in akc:
            novo = copy.deepcopy(st)
            for y in x:
                novo[y] = x[y]
            stanja.append(novo)
        
        return stanja
    
    def is_solved(self, st):
        
        uvjet = True
        
        for x in st:
            if st[x] == "A":
                uvjet = False
                
        return uvjet
        
        
    def is_terminal(self, st):
        GC = (st["goat"] == st["cabbage"] and st["goat"] != st["man"])
        WG = (st["goat"] == st["wolf"] and st["goat"] != st["man"])
        
        return GC or WG
         
    def action(self, ak):
        self.done.append(ak)
        for x in ak:            
            self.dic[x] = ak[x]    
            
    def undo_action(self):
        ak = self.done[len(self.done)-1]
        self.done.remove(ak)
        for x in ak:
            if ak[x] == "A":
                self.dic[x] = "B"
            else:
                self.dic[x] = "A"
        
    def copy(self):
        return copy.deepcopy(self.dic)
   
             
def solution_dfs(m):
    
    stanja = m.next_states(m.dic)
    rod = []
    for x in stanja:
        rod.append([x, m.dic])
    visited = []
    visited.append(m.dic)
    
    while len(stanja)>0:
        visited.append(stanja[0])
        parent = stanja[0]
        
        if m.is_solved(stanja[0]):
            kraj = stanja[0]
            break
        elif m.is_terminal(stanja[0]):
            stanja = stanja[1:]
        else:
            novi = m.next_states(stanja[0])
            stanja = stanja[1:]
            for x in novi:
                if x not in visited:
                    stanja.insert(0, x)
                    rod.append([x,parent])
            
    put = []
    put.append(kraj)
    while(True):
        for x in rod:
            if x[0] == kraj:
                parent = x[1]
        kraj = parent
        put.append(kraj)
        if kraj == m.dic:
            break
    put.reverse()
    
    for x in put:
        print(x)
    
    
def solution_bfs(m):    
        
    stanja = m.next_states(m.dic)
    rod = []
    for x in stanja:
        rod.append([x, m.dic])
    visited = []
    visited.append(m.dic)    
    
    while len(stanja)>0:
        visited.append(stanja[0])
        
        if(m.is_solved(stanja[0])):
            kraj = stanja[0]
            break
        elif(m.is_terminal(stanja[0])):
            stanja = stanja[1:]
        else:
            novi = m.next_states(stanja[0])            
            for x in novi:
                if x not in visited:                    
                    stanja.append(x)
                    rod.append([x,stanja[0]])
            stanja = stanja[1:]
            
    put = []
    put.append(kraj)
    while(True):
        for x in rod:
            if x[0] == kraj:
                parent = x[1]
        kraj = parent
        put.append(kraj)
        if kraj == m.dic:
            break
    put.reverse()
    
    for x in put:
        print(x)
        
def best_first_search(m):
    
    stanja = m.next_states(m.dic)
    heuristika = []
    
    for x in stanja:
        count = 0
        for y in x.values():
            if y == "B":
                count +=1
        heuristika.append([x, count])
        
    heuristika = sort(heuristika)      
        
    rod = []
    for x in stanja:
        rod.append([x, m.dic])
    visited = []
    visited.append(m.dic)
    
    while(len(heuristika)>0):
        
        state = heuristika[0][0]
        
        visited.append(state)
        
        if(m.is_solved(state)):
            kraj = state
            break
        elif(m.is_terminal(state)):
            heuristika = heuristika[1:]
        else:
            novi = m.next_states(state)            
            for x in novi:
                if x not in visited:                    
                    
                    count = 0
                    for y in x.values():
                        if y == "B":
                            count +=1
                    heuristika.append([x,count])   
                    rod.append([x,state])            
            heuristika = heuristika[1:]
            heuristika = sort(heuristika)
            
    put = []
    put.append(kraj)
    while(True):
        for x in rod:
            if x[0] == kraj:
                parent = x[1]
        kraj = parent
        put.append(kraj)
        if kraj == m.dic:
            break
    put.reverse()
    
    for x in put:
        print(x)
        
            
def sort(sub_li):
    sub_li.sort(key = lambda x:x[1], reverse = True)
    return sub_li        
    
def generate(m, akc, visited, rijecnik):
    
    visited.append(m.as_string())
    rijecnik[m.as_string()] = m
    
    for x in akc:        
        m.action(x)
        if(m.as_string() in visited):            
            m.undo_action()            
        else:                        
            ak = m.all_actions(m.dic)            
            generate(m, ak, visited, rijecnik)
            m.undo_action()
            
    return rijecnik
    

st = stanje()   

rc = generate(st, st.all_actions(st.dic), [], {})

for x in rc.keys():
    print(x)






