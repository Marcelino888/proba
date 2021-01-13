# coding=UTF-8

import random
        
#zwraca dwuwymiarową tablice składającą się z podanej ilości wierszy oraz kolumn
def stworzWidok(iloscWierszy, iloscKolumn):
    widok = []

    for i in range(0, iloscWierszy):
        wiersz = []
        for j in range(0, iloscKolumn): 
            wiersz.append(False)
        
        widok.append(wiersz)

    return widok

#ustawia losowe komórki jako zajęte
def wypelnijWidokLosowo(widok, iloscKomorek):
    for i in range(0, iloscKomorek):
        y = random.randrange(0, len(widok) - 1)
        wiersz = widok[y]
        x = random.randrange(0, len(wiersz) - 1)
        wiersz[x] = True

#zwraca informacje o tym czy komórka jest zajęta
def jestKomorkaZajeta(widok, pozycjaKomorki):
    wiersz = widok[pozycjaKomorki["y"] - 1]

    return wiersz[pozycjaKomorki["x"] -1]

#zwraca tylko zajęte komórki z podanej tablicy komórek
def filtrujZajeteKomorki(widok, pozycjeKomorek):
    zajeteKomorki = []

    for pozycjaKomorki in pozycjeKomorek:
        if jestKomorkaZajeta(widok, pozycjaKomorki):
            zajeteKomorki.append(pozycjaKomorki)

    return zajeteKomorki

#zwraca komórki wokół danej komórki
def wezKomorkiWokol(widok, pozycjaKomorki):

    iloscWierszy = len(widok)

    #[x, y]
    kierunki = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1]
    ]

    pozycjeKomorek = []

    for kierunek in kierunki:
        kierunekX = kierunek[0]
        kierunekY = kierunek[1]

        pozycjaKomorkiWokol = {
            "x": pozycjaKomorki["x"] + kierunekX,
            "y": pozycjaKomorki["y"] + kierunekY
        }

        if pozycjaKomorkiWokol["y"] >= 1 and pozycjaKomorkiWokol["x"] >= 1 and pozycjaKomorkiWokol["y"] <= iloscWierszy:
            wiersz = widok[pozycjaKomorkiWokol["y"] -1]
            iloscKolumn = len(wiersz)

            if pozycjaKomorkiWokol["x"] <= iloscKolumn:
                pozycjeKomorek.append(pozycjaKomorkiWokol)
        
    return pozycjeKomorek

#zwraca komórki sąsiednie danej komórki (obok, w tym samym wierszu)
def wezKomorkiSasiednie(widok, pozycjaKomorki):

    iloscWierszy = len(widok)

    #[x, y]
    kierunki = [
        [-1, 0],
        [1, 0]
    ]

    pozycjeKomorek = []

    for kierunek in kierunki:
        kierunekX = kierunek[0]
        kierunekY = kierunek[1]

        pozycjaKomorkiSasiedniej = {
            "x": pozycjaKomorki["x"] + kierunekX,
            "y": pozycjaKomorki["y"] + kierunekY
        }

        if pozycjaKomorkiSasiedniej["y"] >= 1 and pozycjaKomorkiSasiedniej["x"] >= 1 and pozycjaKomorkiSasiedniej["y"] <= iloscWierszy:
            wiersz = widok[pozycjaKomorkiSasiedniej["y"] -1]
            iloscKolumn = len(wiersz)

            if pozycjaKomorkiSasiedniej["x"] <= iloscKolumn:
                pozycjeKomorek.append(pozycjaKomorkiSasiedniej)
        
    return pozycjeKomorek


def renderuj(widok):
    widokString = ""

    for wiersz in widok:
        for komorka in wiersz:
            widokString += "*" if komorka else "."
        
        widokString += "\n"

    print(widokString)

def start():
    #Stworzenie widoku składającego się z 10 wierszy oraz 20 kolumn
    widok = stworzWidok(10, 20)
    
    #Wypełnienie 100 losowych komórek widoku
    wypelnijWidokLosowo(widok, 100)
    
    print("Przed:")
    renderuj(widok)

    for y, wiersz in enumerate(widok):
        for x, komorka in enumerate(wiersz):
            pozycjaKomorki = {
                "x": x + 1,
                "y": y + 1
            }

            if jestKomorkaZajeta(widok, pozycjaKomorki): 
                komorkiWokol = wezKomorkiWokol(widok, pozycjaKomorki)
                komorkiSasiednie = wezKomorkiSasiednie(widok, pozycjaKomorki)

                zajeteKomorkiWokol = filtrujZajeteKomorki(widok, komorkiWokol)    
                zajeteKomorkiSasiednie = filtrujZajeteKomorki(widok, komorkiSasiednie)

                iloscKomorekWokol = len(komorkiWokol)
                iloscZajetychKomorekWokol = len(zajeteKomorkiWokol)
                iloscWolnychKomorekWokol = iloscKomorekWokol - iloscZajetychKomorekWokol
                
                iloscKomorekSasiednich = len(komorkiSasiednie)
                iloscZajetychKomorekSasiednich = len(zajeteKomorkiSasiednie)

                if (iloscWolnychKomorekWokol >= iloscZajetychKomorekWokol) or (iloscZajetychKomorekSasiednich == 0 and (pozycjaKomorki["x"] + pozycjaKomorki["y"]) % 2 != 0):
                    widok[y][x] = True
                else:
                    widok[y][x] = False

    print("Po:")
    renderuj(widok)
  
                
start()