# coding=UTF-8

import math

def obliczDelte(a, b, c):
    return math.pow(b, 2) - 4 * a * c

#(a2+1)x2-(a-1)x=a3
#(a2+1)x2-(a-1)x-a3=0
for a in range(-100, 101):
    aFunkcji = math.pow(a, 2) + 1
    bFunkcji = -1 * (a - 1)
    cFunkcji = -1 * (math.pow(a, 3))

    delta = obliczDelte(aFunkcji, bFunkcji, cFunkcji)

    maRozwiazania = delta >= 0
    
    if maRozwiazania:
        print("Równanie kwadratowe (a2+1)x2-(a-1)x=a3 dla parametru a = {} ma rozwiązania rzeczywiste".format(a))
    else:
        print("Równanie kwadratowe (a2+1)x2-(a-1)x=a3 dla parametru a = {} nie ma rozwiązań rzeczywistych".format(a))