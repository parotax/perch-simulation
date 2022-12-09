import matplotlib.pyplot as plt
from math import cos, sin, pi, sqrt
import random

jarvi = 500

class Kala:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def liikuta(self, dx, dy):
        self.x += dx
        self.y += dy

class Parvi:
    def __init__(self, x, y, vauhti, suunta, r):
        self.x = x
        self.y = y
        self.paikatX = [self.x]
        self.paikatY = [self.y]
        self.kalat = []
        self.vauhti = vauhti
        self.suunta = suunta
        self.r = r

    def lisaa_kala(self):
        alpha = 2 * pi * random.random()
        r = self.r * sqrt(random.random())
        x = r * cos(alpha) + self.x
        y = r * sin(alpha) + self.y
        kala = Kala(x, y)
        self.kalat.append(kala)

    def liiku(self):
        self.suunta += random.uniform(-1.0 , 1.0)
        
        dx = self.vauhti*sin(self.suunta)
        dy = self.vauhti*cos(self.suunta)

        if self.x + dx <= self.r or self.y + dy <= self.r or self.x + dx >= jarvi - self.r or self.y + dy >= jarvi - self.r:
            self.liiku()
            return

        self.x += dx
        self.y += dy

        for kala in self.kalat:
            kala.liikuta(dx, dy)

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

kalat = Parvi(jarvi / 2, jarvi / 2, 15, 0, 5)

for i in range(6):
    kalat.lisaa_kala()
kalat.liiku()
piirrareitti(kalat.paikatX, kalat.paikatY)
