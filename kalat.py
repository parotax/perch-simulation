from math import cos, sin, pi, sqrt
import random

jarvi = 400

class Kala:
    id = 1
    def __init__(self, x, y): 
        self.id = Kala.id
        Kala.id += 1
        self.x = x
        self.y = y

    def liikuta(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return f"Kala id {self.id} ({self.x}, {self.y})"

class Parvi:
    id = 0
    def __init__(self, x, y, suunta, r):
        self.id = Parvi.id
        Parvi.id += 1
        self.x = x
        self.y = y
        self.paikatX = [self.x]
        self.paikatY = [self.y]
        self.kalat = []
        self.vauhti = 2
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

    def __str__(self):
        return f"Parvi {len(self.kalat)} kalaa ({self.x}, {self.y})"

    def tuhoa(self, id):
        for kala in self.kalat:
            if kala.id == id:
                self.kalat.remove(kala)
