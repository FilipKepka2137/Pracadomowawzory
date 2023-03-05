import time, random
from bohater import bohaterr

print("Jakiego bohatera chcesz wybierasz")
print("A - Lis    B - Wilk ")
odp = input("Odp = ")

if odp == "A":
    lis = bohaterr("zbigniew", 10, 3, "paczka papierosów", "smierc")

    print(f"'imie'{lis.name}\t'kryształki'{lis.crystals}\t'zycia'{lis.lives}\t'plecak'{lis.backpack}\t'cel'{lis.goal}\t")
    print("=="*68)        
    print("Masz ze sobą mape. Dalej trzeba iść po lesie. Na drodze spotykasz Swojego starego z bojowym zadaniem - musisz zagrac z nim gre... Co zrobisz?")
    print("Trzeba grać w grę - Papier, kamień, nożyce ")
    print("Wiedz, że jeśli wygrasz to możesz dostać 5 Krzyształów włodzimierza bialego a jeśli przegrasz, on cię zje ")

    while True:
        variant = input("Wybierz: kamień, nożyce czy papier? (z małą literą)")
        time.sleep(1)                
        print("Sprawdzanie pisowni...")
        time.sleep(1)
        #variant to kto wprowadza a comp = Thanos
        if variant == "kamień" or variant == "nożyce" or variant =="papier" :
            print("Wszystko jest poprawne. Gra trwa.")
            time.sleep(1)
            print("Teraz Thanos dokonuje wyboru...")
            comp = random.randint(1, 3)
            if comp == 1:
                comp = "kamień"
            elif comp == 2:
                    comp == "nożyce"
            else:
                comp = "papier"
                time.sleep(1)
                print("Wybór został dokonany.")
                time.sleep (1)
                print("Gra się rozpoczyna!")
                time.sleep(1)
                print ("1 - kamień...")
                time.sleep(1)
                print("2 - nożyce...")
                time.sleep (1)
                print("3 - papier...")
                    
                if variant == "papier" and comp == "kamień":
                    print("Stary wybrał kamień...")
                    print("Wygrałeś i pokonałeś Starego i dostałeś 5 krzyształów włodzimierza białego")
                    print()
                    time.sleep(1)
                    lis.crystals += 5
                    print(f"'imie'{lis.name}\t'kryształki'{lis.crystals}\t'zycia'{lis.lives}\t'plecak'{lis.backpack}\t'cel'{lis.goal}\t")

                    print("Znalazłeś skarb w piwnicy. Za 15 Krzyształów dostaniesz skarb z millionami kryształów ")
                    

                elif variant == "kamień" and comp =="nożyce": 
                    print("Stary wybrał nożyczki... ") 
                    print("Wygrałeś(łaś) i zabiłeś(łaś) Starego i dostałeś(łaś) 5 krzyształów")
                    print()
                    time.sleep(1)
                    lis.crystals += 5
                    print(f"'imie'{lis.name}\t'kryształki'{lis.crystals}\t'zycia'{lis.lives}\t'plecak'{lis.backpack}\t'cel'{lis.goal}\t")
                    print("Znalazłeś skarba w Grenlandii. Za 15 Krzyształów dostaniesz skarb z millionami brilliantów ")
                    
                elif variant == "nożyce" and comp == "papier":
                    print("Stary wybrał papier...")
                    print("Wygrałeś(łaś) i zabiłeś(łaś) Stary i dostałeś(łaś) 5 krzyształów")
                    print()
                    time.sleep(1)
                    lis.crystals += 5
                    print(f"'imie'{lis.name}\t'kryształki'{lis.crystals}\t'zycia'{lis.lives}\t'plecak'{lis.backpack}\t'cel'{lis.goal}\t")
                    print("Znalazłeś skarba w Grenlandii. Za 15 Krzyształów dostaniesz skarb z millionami brilliantów ")
                    
                elif variant == comp: 
                    print("Stary wybrał", comp, ". . .") 
                    time.sleep (1)
                    print("Remis!")
                    print()
                    time.sleep (1)
                    print(f"'imie'{lis.name}\t'kryształki'{lis.crystals}\t'zycia'{lis.lives}\t'plecak'{lis.backpack}\t'cel'{lis.goal}\t")
                else: 
                    print("Stary wybrał", comp, ". . .")   
                    time.sleep (1)
                    print("Przegrałeś!")
                    print("On cię zjadł")
                    print(f"'imie'{lis.name}\t'kryształki'{lis.crystals}\t'zycia'{lis.lives}\t'plecak'{lis.backpack}\t'cel'{lis.goal}\t")
                    
                          
    else:
        print("Nie ma takiej komendy")

#B - Wilk = informacja
elif odp == "B":
    wilk = bohaterr("bożydar", 10, 3, "pistolet i 10kg c4, 5 gramów mety", "ćpanie")
    print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")
    
    print()
    print("Jesteś w statku. Na ręce masz mapa, żeby znaleść skarb musisz wybrać poprawną odpowiedż na zagadkę, są trzy opcji.  ")
    print("Masz tylko jedną próba. Za niepoprawną sracisz 5 KRZYSZTAŁÓW i Jedną życia. ")
    print("Jeśli wygrasz dostaniesz 5 KRZYSZTAŁÓW")
    print("Największa wyspa na świecie?")
    print("A - Nowa Gwinea   B - Borneo   C - Grenlandia")
    odpow = input("Opd =")
    if odpow == "A":
        print("Odpowiedż jest niepoprawna!!!!!!")
        print("Straciłaś(łeś) 5 krzyształów i życia")

        wilk.lives += 2
        print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")
    elif odpow == "B":
        print("Odpowiedż jest niepoprawna!!!!!!")
        print("Straciłaś(łeś) 5 krzyształów i życia")
        wilk.lives = 2
        print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")
    elif odpow == "C":
        print("Gratuluję odpowiedż jest poprawna!!!!!!") 
        print("Dostałaś(łeś) 5 krzyształów")
        wilk.crystals += 5
        print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")
        print("Płynieś statkem do Grenlandii.")    
        print("Już jesteś w Grenlandii ")
        print("Skąd pochodzili mieszkańcy Grenlandii ")            
        print("A - Azja Środkowa   B - Azja poludniowo wschodnia   C - Azja poludniowa")
        odpowi = input("Odp =")
        if odpowi == "A":
                print("Gratuluję odpowiedż jest poprawna!!!!!!") 
                print("Dostałaś(łeś) 5 krzyształów")
                wilk.crystals += 5
                print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")
                print("Znalazłeś skarba w Grenlandii. Za 25 Krzyształów dostaniesz skarb w którym milliard brilliantów ")
                
        elif odpowi == "B":
                print("Odpowiedż jest niepoprawna!!!!!!")
                print("Straciłaś(łeś) 5 krzyształów i życia")
                wilk.lives -= 1
                print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")
                print("Nieznalazłeś skarba w Grenlandii. Za 5 Krzyształów dostaniesz skarb w którym million brilliantów ")    
        elif odpowi == "C":
                print("Odpowiedż jest niepoprawna!!!!!!")
                print("Straciłaś(łeś) 5 krzyształów i życia")
                wilk.crystals -= 5
                wilk.lives -= 2
                print(f"'imie'{wilk.name}\t'kryształki'{wilk.crystals}\t'zycia'{wilk.lives}\t'plecak'{wilk.backpack}\t'cel'{wilk.goal}\t")        

                print("Nieznalazłeś skarba w Grenlandii. Za 5 Krzyształów dostaniesz skarb w którym million brilliantów ")


        else:
                print("Nie ma takiej komendy")        

else:
    print("Nie ma takiej komendy") 