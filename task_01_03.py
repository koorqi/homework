# -*- coding: utf-8 -*-
ch1=int(input('введите чиcло 1:'))
ch2=int(input('введите чиcло 2:'))
ch3=int(input('введите чиcло 3:'))
lst=[ch1,ch2,ch3]
n=1
while n<len(lst):
    for i in range(len(lst)-n):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1], lst[i]
    n+=1
print (lst)
    
#используем метод "пузырька"

'''
b=min(lst)
print (b)
a=max(lst)
print (a)
'''

#lst.sort()
#print (lst)


