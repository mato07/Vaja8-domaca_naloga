# -*- coding: utf-8 -*-
#Pretvornik iz kilometrov v milje in obratno

print "Pozdravljen, sem pretvornik razdalje iz kilometrov v milje in nazaj."

pretvornik = 1.6

while True:
    razdalja = float(raw_input("Vnesi razdaljo, ki jo želiš pretvoriti: "))
    pogoj = int(raw_input("Za pretvorbo iz km v milje vnesi 0, za pretvorbo iz milj v km pa 1: "))

    if pogoj == 0:
        p0 = razdalja * pretvornik
        print p0, "km"
        nadaljevanje = raw_input("Če želiš narediti še kakšno pretvorbo vnesi da, če ne, pa vnesi ne: ")
        if nadaljevanje == "da":
            continue
        elif nadaljevanje == "ne":
            break
        else:
            print "Vnešena zahteva za pretvorba je napačna"
            print "Poskusi znova!"
    elif pogoj == 1:
        p1 = razdalja / pretvornik
        print p1, "mi"
        nadaljevanje = raw_input("Če Želiš narediti še kakšno pretvorbo vnesi da, če ne, pa vnesi ne: ")
        if nadaljevanje == "da":
            continue
        elif nadaljevanje == "ne":
            break
        else:
            print "Vnešena zahteva za pretvorba je napačna"
    else:
        print "Vnešena zahteva za pretvorba je napačna!"