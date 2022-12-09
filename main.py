import matplotlib.pyplot as plt
from math import cos, sin
import random

jarvi = [(0, 0), (1000, 0), (1000, 500), (0, 500)]

class Kala:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

class Parvi:
    def __init__(self, kalat, vauhti, x, y, suunta):
        self.x = x
        self.y = y
        self.paikatX = [self.x]
        self.paikatY = [self.y]
        self.kalat = kalat
        self.vauhti = vauhti
        self.suunta = suunta

    def liiku(self):
        self.suunta += random.uniform(-1.0 , 1.0)
        
        dx = self.vauhti*sin(self.suunta)
        dy = self.vauhti*cos(self.suunta)
        
        self.x += dx
        self.y += dy

        self.paikatX.append(self.x)
        self.paikatY.append(self.y)

def piirrareitti(xlista, ylista):
    
    fig, ax = plt.subplots()
    ax.plot(xlista, ylista,'o')
    ax.set(xlabel='x', ylabel='y',
    title='Parven reitti')
    ax.grid()

   
    ax.set_xlim([0-5, 500+5])   # Piirretään symmetrisesti origon ympärille
    ax.set_ylim([0-5, 1000+5])
    
    plt.show()

kalat = Parvi([], 1, 250, 500, 0)

for i in range(20):
    kalat.liiku()

piirrareitti(kalat.paikatX, kalat.paikatY)
