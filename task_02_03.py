def average(lst):
    l=len(lst) #кол-во элементов
    s=sum(lst) #сумма элементов списка
    sa=float(s/l)
    return round(sa,3) #округляем 

#print (average([1,2,3,4,5,6,7,8,9,10,666]))

