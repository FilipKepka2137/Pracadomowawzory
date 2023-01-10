from math import pi
class Matma:
    @staticmethod
    def odlegloscruchjednostajny():
        xo = float(input("xo = "))
        vo = float(input("vo = "))
        t = float(input("t = "))
        a = float(input("a = "))
        print(f"Wynik to {xo+vo*t+0,5*a*t*t}")
    def czestotliwosc():
        n = float(input("n="))
        t = float(input("t="))
        print(f"Wynik to {n/t} Hz.")
    def predkosckontowa():
        kat = float(input("kat="))
        t = float(input("t="))
        print(f"Wynik to {kat/t}")
    def chwilowapredkosckatowa():
        kat = float(input("kat="))
        t = float(input("t="))
        print(f"Wynik to {kat/t} Hz.")
    def chwilowapredkosckatowazmiana():
        pkat = float(input("zmiana prędkości kątowej = "))
        t = float(input("t="))
        print(f"Wynik to {pkat/t}")
    def predkoscliniowa():
        r= float(input("r = "))
        tt = float(input("T = "))
        print(f"Wynik to {2*pi*r/tt}")
    def plpredkoscliniowazpkatowej():
        w = float(input("w = "))
        r = float(input("r = "))
        print(f"Wynik to {w*r}")
    def przyspieszeniesrednie():
        v = float(input("roznica v"))
        t = float(input("roznica t = "))
        print(f"Wynik to {v/t}")
    def silawypadkowa():
        m = float(input("masa = "))
        a = float (input("przyspieszenie = "))
        print(f"Wynik to {m*a}")
    def przyspieszeniefim():
        ff = float(input("f = "))
        m = float(input("m = "))
        print(f"Wynik to {ff/m}")
    def zamaiananakm():
        xxx = float(input(":"))
        
        print(f"Wynik to {xxx*1000/3600} m/s.")  
    def zmianatnag():
        xxx = float(input(":"))
        print(f"Wynik to {xxx*1000000}")
    def predkosc():
        s = float(input("(m)"))
        t = float(input("(s)"))
        print(f"Wynik to {s/t}m/s")
    def czaszpredkosci():
        v = float(input("(m/s)"))
        s = float(input("(m)"))
        print(f"Czas to {s/v}")
    def drogazpredkosci():
        v = float(input("(m/s)"))
        t = float(input("(s)"))
        print(f"Droga to {t*v} s.")
    def predkoscsrednia():
        s = float(input("(m)"))
        t = float(input("(s)"))
        print(f"Prędkość średnia {s/t} m/s")
    def przyspierszenie():
        v = float(input("(m/s)"))
        t = float(input("(s)"))
        print(f"Wynik to {v/t}")
    def predkosczprzyspieszenia():
        vo = float(input("vo = "))
        a = float(input("a = "))
        t = float(input("t = "))
        print(f"Wynik to {vo+a*t}")