from wzorki import Matma


print("""
Jaka akcje chcesz wykonac?????????????
1 = odleglosc w ruchu jednostajnym prostoliniowym
2 = częstotliwość
3 = prędkośc kątowa
4 = chwilowa prędkość kątowa
5 = chwilowa prędkość kątowa
6 = prędkość liniowa
7 = prędkość liniowa z kątowej
8 = pszyspieszenie srednie
9 = siła wypadkowa
10 = przyspieszenie
11 = przeliczanie z km/h na m/s
12 = zamiana z t na g
13 = obliczanie predkosci (s,t)
14 = obliczanie czasu z prędkości
15 = obliczanie drogi z prędkości
16 = obliczanie prędkości średniej
17 = przyspieszenie
18 = obliczanie prędkości po przyspieszeniu
""")
zzzz = int(input(""))
if zzzz == 1:
    Matma.odlegloscruchjednostajny()
elif zzzz ==2 :
    Matma.czestotliwosc()
elif zzzz == 3:
    Matma.predkosckontowa()
elif zzzz == 4:
    Matma.chwilowapredkosckatowa()
elif zzzz == 5:
    Matma.chwilowapredkosckatowazmiana()
elif zzzz == 6:
    Matma.predkoscliniowa()
elif zzzz == 7:
    Matma.plpredkoscliniowazpkatowej()
elif zzzz == 8:
    Matma.przyspieszeniesrednie()
elif zzzz == 9:
    Matma.silawypadkowa()
elif zzzz == 10:
    Matma.przyspieszeniefim()
elif zzzz == 11:
    Matma.zamaiananakm()
elif zzzz == 12:
    Matma.zmianatnag()
elif zzzz == 13:
    Matma.predkosc()
elif zzzz == 14:
    Matma.czaszpredkosci()
elif zzzz == 15:
    Matma.drogazpredkosci()
elif zzzz == 16:
    Matma.predkoscsrednia()
elif zzzz == 17:
    Matma.przyspierszenie()
elif zzzz == 18:
    Matma.predkosczprzyspieszenia()