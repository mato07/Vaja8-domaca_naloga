# -*- coding: utf-8 -*-

konec = int(raw_input("Vnesi število od 1 do 100: "))

for i in range(1,konec+1):
    if i%3 == 0:
        if i%5 != 0:
            print "fizz"
        else:
            print "fizzbuzz"
    elif i%5 == 0:
        print "buzz"
    else:
        print i