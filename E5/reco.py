# reco.py
import sys,os

# PASSO 2
class Hit:
    '''
    Un oggetto di tipo Hit deve contenere informazioni su:
        - Id Modulo;
        - Id Sensore;
        - Time Stamp rivelazione.

    Oggetti di tipo Hit devono essere ordinabili in base al Time Stamp 
    ed eventualmente in base alla Id del Modulo e del Sensore.
    '''
    def __init__(self, md, dect, ht):
        self.id_module= md
        self.id_detector=dect
        self.hit_time_rev= ht

    def __repr__(self):
        return 'Module: {:} __ Detector: {:} __ hit_time {:}'.format(self.id_module, self.id_detector, self.hit_time_rev)
    
    def __str__(self):
        return 'Module: {:} -- Detector: {:} -- hit_time {:}'.format(self.id_module, self.id_detector, self.hit_time_rev)

    def __eq__(self, other):
        return self.hit_time_rev == other.hit_time_rev
    
    def __lt__(self, other):
        return self.hit_time_rev < other.hit_time_rev
    
    def __gt__(self, other):
        return self.hit_time_rev > other.hit_time_rev
    
    def __sub__(self, other):
        return self.hit_time_rev - other.hit_time_rev
    
    def __add__(self, other):
        return self.hit_time_rev + other.hit_time_rev

    def pos_module(self, other): #ordina 2 hit time in base al modulo dal quale sono stati rilevati
        ord = False
        if(self.id_module<other.id_module or self.id_module==other.id_module):
            ord=True
        return ord
        
    def pos_detector(self, other): #ordina 2 hit time in base al sensore dal quale sono stati rivelati (se sono relativi a 2 moduli diversi prevale il numero del modulo)
        ord=False
        if(self.id_module == other.id_module):
            ord = self.id_detector < other.id_detector
        else:
            ord = self.pos_module(self,other)
        return ord
    
    def ord_module(self, other): #ordina 2 hit time uguali in base al modulo dal quale sono stati rivelati.
        ord = False
        if (self.hit_time_rev == other.hit_time_rev):
            ord= self.pos_module(self, other)
        return ord
        
    def ord_detector(self, other): #ordina 2 hit time uguali in base al sensore dal quale sono stati rilevati(se sono relativi a due moduli diversi prevale il numero del modulo)
        ord= False
        if (self.hit_time_rev == other.hit_time_rev):
            if(self.id_module == other.id_module):
                ord = self.id_detector < other.id_detector
            else:
                ord = self.pos_module(self, other)              
        return ord

    




        