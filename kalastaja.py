import random
from math import sin, cos

jarvi = 500

class Kalastaja:
    def __init__(self, x, y, vauhti, suunta):
        self.x = x
        self.y = y
        self.vauhti = vauhti
        self.suunta = suunta
        self.status = "Kairaa"
        self.kalastanut = 0
        self.paikatX = [self.x]
        self.paikatY = [self.y]

    def liiku(self):
        self.suunta += random.uniform(-1.0 , 1.0)
        
        dx = self.vauhti*sin(self.suunta)
        dy = self.vauhti*cos(self.suunta)

        if self.x + dx <= 0 or self.y + dy <= 0 or self.x + dx >= jarvi or self.y + dy >= jarvi:
            self.liiku()
            return


        self.x += dx
        self.y += dy
        self.paikatX.append(self.x)
        self.paikatY.append(self.y)
        self.status = "Kairaa"

    def kairaa(self):
        self.status = "Kalastaa"

    def kalasta(self):
        self.kalastanut += 1
        if self.kalastanut > 2:
            self.vaihda_paikkaa()
    
    def vaihda_paikkaa(self):
        self.status = "Liikkuu"
        self.liiku()
