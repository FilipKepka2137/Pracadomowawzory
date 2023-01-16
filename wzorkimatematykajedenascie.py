from janpaweldwa import Matematycznewzorkipracadomowa



print('CO LICZYMY??? \n 1 - OBJĘTOŚĆ SZEŚCIANU \n 2 - POLE SZEŚCIANU \n 3 - POLE CAŁKOWITE SZEŚCIANU \n 4 - OBJĘTOŚĆ PROSTOPADŁOŚCIANU \n 5 - POLE PROSTOPADŁOSCIANU \n 6 - POLE CAŁKOWITE PROSTOPADŁOSCIANU \n 7 - OBJETOSC GRANIASTOSLUPA \n 8 - POLE GRANIASTOSŁUPA \n 9 - POLE CAŁKOWITE GRANIASTOSŁUPA \n 10 - OBJETOSC OSTROSLUPA \n 11 - POLE OSTROSŁUPA')



inp = int(input())



if inp == 1:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),0,0,0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.objszescian()



if inp == 2:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),0,0,0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.p_szescianu()



if inp == 3:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),0,0,0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.pc_szescianu()



if inp == 4:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),float(input('Daj y ')),float(input('Daj z ')),0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.obj_prostopadloscian()



if inp == 5:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),float(input('Daj y ')),float(input('Daj z ')),0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.p_prostopadloscian()



if inp == 6:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),float(input('Daj y ')),float(input('Daj z ')),0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.pc_prostopadloscianu()



if inp == 7:
    xxx = Matematycznewzorkipracadomowa(0,0,0,0,float(input('Daj h ')),float(input('Daj p-podstawy ')),0)
    lista = [xxx]
    for obj in lista:
        obj.obj_graniastoslup()



if inp == 8:
    xxx = Matematycznewzorkipracadomowa(0,0,0,0,0,float(input('Daj p_podstawy ')),float(input('Daj p_boków ')))
    lista = [xxx]
    for obj in lista:
        obj.p_graniastoslup()



if inp == 9:
    xxx = Matematycznewzorkipracadomowa(float(input('Daj x ')),float(input('Daj y ')),float(input('Daj z ')),0,0,0,0)
    lista = [xxx]
    for obj in lista:
        obj.pc_graniastoslup()



if inp == 10:
    xxx = Matematycznewzorkipracadomowa(0,0,0,0,float(input('Daj h ')),float(input('Daj p_podstawy ')),0)
    lista = [xxx]
    for obj in lista:
        obj.obj_ostroslup()


        
if inp == 11:
    xxx = Matematycznewzorkipracadomowa(0,0,0,0,0,float(input('Daj p_podstawy ')),float(input('Daj p_boków ')))
    lista = [xxx]
    for obj in lista:
        obj.p_ostroslup()