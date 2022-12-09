import matplotlib.pyplot as plt
from kalat import Parvi
from kalastaja import Kalastaja
from random import randint
import settings

settings.init()
jarvi = 400

def piirrareitti(xlista, ylista, title):
    fig, ax = plt.subplots()
    ax.plot(xlista, ylista,'o')
    ax.set(xlabel='x', ylabel='y', title=title)
    ax.grid()
   
    ax.set_xlim([0-5, jarvi+5])
    ax.set_ylim([0-5, jarvi+5])
    
    plt.show()

for i in range(15):

    jukka = Kalastaja(25, 25, 0)

    for i in range(10):
        kalat = Parvi(randint(50, jarvi - 50), randint(50, jarvi - 50), 0, 5)

        for j in range(15):
            kalat.lisaa_kala()

        settings.parvet.append(kalat)

    for i in range(300):
        for parvi in settings.parvet:
            parvi.liiku()

        if jukka.status == "Kalastaa": jukka.kalasta()
        elif jukka.status == "Kairaa": jukka.kairaa()
        elif jukka.status == "Liikkuu": jukka.vaihda_paikkaa()

    print(jukka.saalista)
