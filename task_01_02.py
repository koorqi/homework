# -*- coding: utf-8 -*-
sum_tarelok=int(input("Введите кол-во тарелок:"))
sum_sredstvo=float(input("Введите кол-во средства:"))
if sum_tarelok<=0 or sum_sredstvo<=0:
    print ('неверный ввод')



while sum_sredstvo >0 and sum_tarelok >0:
    sum_sredstvo=sum_sredstvo-0.5
    sum_tarelok=sum_tarelok-1
    if sum_sredstvo==0 and sum_tarelok==0:
        print('Все тарелки вымыты, моющее средство закончилось')
        break
    if sum_sredstvo>0 and sum_tarelok==0:
        print ('Все тарелки вымыты. Осталось',sum_sredstvo,'едениц моющего стредства')
        break
    if sum_sredstvo==0 and sum_tarelok>0:
        print ('Моющее стредство закончилось, осталось', sum_tarelok, 'тарелок')
        
