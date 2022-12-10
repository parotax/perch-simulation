from kalat import Parvi
from kalastaja import Kalastaja
from random import randint
import settings

settings.init()
jarvi = 400
time = 300
parvienMaara = 10
kalojaParvessa = 15
ajaKertoja = 25

def printResults(results):
    print(len(results))

result = []

for i in range(ajaKertoja):

    jukka = Kalastaja(25, 25, 0)

    for i in range(parvienMaara):
        kalat = Parvi(randint(20, jarvi - 20), randint(20, jarvi - 20), 0, 5)

        for j in range(kalojaParvessa):
            kalat.lisaa_kala()

        settings.parvet.append(kalat)

    for i in range(time):
        for parvi in settings.parvet:
            parvi.liiku()

        if jukka.status == "Kalastaa": jukka.kalasta()
        elif jukka.status == "Kairaa": jukka.kairaa()
        elif jukka.status == "Liikkuu": jukka.vaihda_paikkaa()

    print(jukka.saalista)
    result.append(jukka.saalista)
    settings.parvet.clear()

printResults(result)
