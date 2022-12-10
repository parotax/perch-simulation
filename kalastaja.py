import random
from math import sin, cos, sqrt
import settings

jarvi = 400
kalojenNakokentta = 4

class Kalastaja:
    def __init__(self, x, y, suunta):
        self.x = x
        self.y = y
        self.vauhti = 100
        self.suunta = suunta
        self.status = "Kairaa"
        self.ajastin = 0
        self.paikatX = [self.x]
        self.paikatY = [self.y]
        self.saalista = 0

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
        self.ajastin += 1

        kalaa = False
        for parvi in settings.parvet:
            if abs(parvi.x - self.x) < parvi.r + kalojenNakokentta or abs(parvi.x - self.x) < parvi.r + kalojenNakokentta:
                continue
            for kala in parvi.kalat:
                x = kala.x + parvi.x
                y = kala.y + parvi.y
                if sqrt((x - self.x)**2 + (y - self.y)**2) < kalojenNakokentta:
                    if random.randint(1, 6) == 1:
                        self.saalista += 1
                        parvi.tuhoa(kala.id)
                        self.ajastin = 0
                        kalaa = True
                        break
            if kalaa: break

        if self.ajastin > 10:
            self.status = "Liikkuu"
            self.ajastin = 0
            self.vaihda_paikkaa()
    
    def vaihda_paikkaa(self):
        self.ajastin += 1
        if self.ajastin > 2:
            self.liiku()
            self.ajastin = 0

    def __str__(self):
        return f"Kalastaja {self.saalista} kalaa ({self.x}, {self.y})"
