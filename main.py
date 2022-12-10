from kalat import Parvi
from kalastaja import Kalastaja
from random import randint
import settings

settings.init()
jarvi = 400
testTime = 120
kalojaParvessa = 125
kalaJarvessa = 2200 * jarvi / 100
ajaKertoja = 25

def printResults(results):
    print(len(results))

result = []

for i in range(ajaKertoja):

    kaloja = 0
    jukka = Kalastaja(25, 25, 0)
    stop = False

    while True:
        kalat = Parvi(randint(20, jarvi - 20), randint(20, jarvi - 20), 0, 5)

        for j in range(kalojaParvessa + randint(-75, 75)):
            kalat.lisaa_kala()
            kaloja += 1
            if kaloja == kalaJarvessa: 
                stop = True
                break

        settings.parvet.append(kalat)
        if stop: break

    for i in range(testTime):
        for parvi in settings.parvet:
            parvi.liiku()

        if jukka.status == "Kalastaa": jukka.kalasta()
        elif jukka.status == "Kairaa": jukka.kairaa()
        elif jukka.status == "Liikkuu": jukka.vaihda_paikkaa()

    print("Saalista:", jukka.saalista)
    result.append(jukka.saalista)
    settings.parvet.clear()
    print(time.time() - start)

printResults(result)
