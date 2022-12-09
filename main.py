import matplotlib.pyplot as plt
from math import cos, sin
import random

jarvi = 500

class Kala:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

class Parvi:
    def __init__(self, x, y, kalat, vauhti, suunta, rad):
        self.x = x
        self.y = y
        self.paikatX = [self.x]
        self.paikatY = [self.y]
        self.kalat = kalat
        self.vauhti = vauhti
        self.suunta = suunta
        self.rad = rad

    def liiku(self):
        self.suunta += random.uniform(-1.0 , 1.0)
        
        dx = self.vauhti*sin(self.suunta)
        dy = self.vauhti*cos(self.suunta)

        if self.x + dx <= self.rad or self.y + dy <= self.rad or self.x + dx >= jarvi - self.rad or self.y + dy >= jarvi - self.rad:
            self.liiku()
            return

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

   
    ax.set_xlim([0-5, jarvi+5])   # Piirretään symmetrisesti origon ympärille
    ax.set_ylim([0-5, jarvi+5])
    
    plt.show()

kalat = Parvi(jarvi / 2, jarvi / 2, [], 1, 0, 5)

for i in range(10):
    kalat.liiku()

piirrareitti(kalat.paikatX, kalat.paikatY)
