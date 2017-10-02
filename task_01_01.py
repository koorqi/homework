# -*- coding: utf-8 -*-

sotka=float(input("Введите площадь участка в сотках:"))
if sotka <0:
    print ("Ошибка ввода")
    
else:
    gryadka=15*25
    sotkam2=sotka*100
    kolvo_gryadok=int(sotkam2/gryadka)
    print ("количество грядок:",kolvo_gryadok)
    ostatok= int(sotkam2-gryadka*kolvo_gryadok)
    print ("неиспользованные метры:",ostatok,"m2")
