# -*- coding: utf-8 -*-
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())

len1=((x1-x2)**2)+((y1-y2)**2)
len2=((x1-x3)**2)+((y1-y3)**2)
len3=((x2-x3)**2)+((y2-y3)**2)
#print (len1,len2,len3)
if len1==len2 or len2==len3 or len1==len3:
    print ('прямоугольный')
else:
    print ('Не прямоугольный')
