import matplotlib.pyplot as plt
from kalat import Parvi
from kalastaja import Kalastaja

jarvi = 500

def piirrareitti(xlista, ylista, title):
    fig, ax = plt.subplots()
    ax.plot(xlista, ylista,'o')
    ax.set(xlabel='x', ylabel='y',
    title=title)
    ax.grid()

   
    ax.set_xlim([0-5, jarvi+5])
    ax.set_ylim([0-5, jarvi+5])
    
    plt.show()

jukka = Kalastaja(25, 25, 1, 0)

kalat = Parvi(jarvi / 2, jarvi / 2, 15, 0, 5)

kalat.lisaa_kala()
kalat.lisaa_kala()
kalat.lisaa_kala()

for i in range(6):
    kalat.liiku()

    if jukka.status == "Kalastaa": jukka.kalasta()
    elif jukka.status == "Kairaa": jukka.kairaa()
    elif jukka.status == "Liikkuu": jukka.vaihda_paikkaa()

piirrareitti(kalat.paikatX, kalat.paikatY, "Parven reitti")
piirrareitti(jukka.paikatX, jukka.paikatY, "Jukan reitti")
