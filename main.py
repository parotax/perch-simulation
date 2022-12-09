from math import cos, sin
import random

class Kala:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Parvi:
    def __init__(self, kalat, vauhti, x, y, suunta):
        self.kalat = kalat
        self.vauhti = vauhti
        self.x = x
        self.y = y
        self.suunta = suunta

    def liiku(self):
        self.suunta += random.uniform(-1.0 , 1.0)
        
        dx = self.vauhti*sin(self.suunta)
        dy = self.vauhti*cos(self.suunta)
        
        self.x += dx
        self.y += dy
