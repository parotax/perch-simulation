from kalat import Parvi
from kalastaja import Kalastaja
from random import randint
import settings
from math import sqrt

settings.init()

def printResults(results):
    print("Parametrit")
    print(f"Järven koko: {settings.jarvi}")
    print(f"Pilkkimisen kesto minuutteina: {settings.testTime}")
    print(f"Kalojen määrä parvessa: {settings.kalojaParvessa}")
    print(f"Kalojen määrä järvessä: {int(settings.kalojaJarvessa)}")
    print(f"Kalojen näkökenttä: {settings.kalojenNakokentta}")
    print(f"Toistoja: {settings.ajaKertoja}")
    print(f"Pilkkimisaika saman reiän äärellä minuutteina: {settings.kalastajanKarsivallisyys}")
    print()

    summa = 0
    nollat = 0
    keskiarvo = sum(results) / len(results)
    print(f"keskiarvo on {keskiarvo}")
    for i in results:
        summa += (i - keskiarvo)**2
        if i == 0: nollat += 1
    keskihajonta = sqrt(summa / len(results))
    print(f"keskihajonta on {keskihajonta}")
    print(f"Nollatuloksia: {nollat}")

results = []

for i in range(settings.ajaKertoja):

    kaloja = 0
    jukka = Kalastaja(25, 25, 0)
    stop = False

    while True:
        kalat = Parvi(randint(20, settings.jarvi - 20), randint(20, settings.jarvi - 20), randint(0, 6))

        for j in range(settings.kalojaParvessa + randint(-75, 75)):
            kalat.lisaa_kala()
            kaloja += 1
            if kaloja == settings.kalojaJarvessa: 
                stop = True
                break

        settings.parvet.append(kalat)
        if stop: break

    for i in range(settings.testTime):
        for parvi in settings.parvet:
            parvi.liiku()

        if jukka.status == "Kalastaa": jukka.kalasta()
        elif jukka.status == "Kairaa": jukka.kairaa()
        elif jukka.status == "Liikkuu": jukka.vaihda_paikkaa()

    print("Saalista:", jukka.saalista)
    results.append(jukka.saalista)
    settings.parvet.clear()

printResults(results)
