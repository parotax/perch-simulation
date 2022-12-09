import matplotlib.pyplot as plt
from kalat import Parvi

jarvi = 500

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
