def init():
    global parvet
    global jarvi
    global testTime
    global kalojaParvessa
    global kalojaJarvessa
    global ajaKertoja
    global kalojenNakokentta
    global kalastajanKarsivallisyys
    global kalojenNopeus
    global parvenSade

    parvet = []
    jarvi = 400
    testTime = 120
    kalojaParvessa = 100
    kalojaJarvessa = 1000 * jarvi / 100
    ajaKertoja = 100
    kalastajanKarsivallisyys = 15

    # Muokattavat parametrit alla
    kalojenNakokentta = 4
    kalojenNopeus = 2
    parvenSade = 5
