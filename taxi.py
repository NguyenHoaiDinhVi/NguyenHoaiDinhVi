# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:19:13 2024

@author: nguyenhoaidinhvi
"""
print("tính tiền taxi nè")
x= float(input("nhập số km đi được:"))
if 0<x<=1:
    money=x*20
    if money>100:
        print("tiền taxi là:",money*0.92)
        tien=money*0.92
        print("tiền taxi là:",tien)
    else:
        print("tiền taxi là:",money)
elif 1<x<4:
    money=20+ ((x-1)*13)
    if money>100:
        print("tiền taxi là:",money*0.92)
        tien=money*0.92
        print("tiền taxi là:",tien)
    else:
        print("tiền taxi là:",money)
elif 4<=x<=8:
    money= 20+(13*2)+ ((x-3)*12)
    if money>100:
        print("tiền taxi là:",money*0.92)
        tien=money*0.92
        print("tiền taxi là:",tien)
    else:
        print("tiền taxi là:",money)
elif x>8:
    money= 20+(13*2)+(10*6)+((x-8)*10)
    if money>100:
        print("tiền taxi là:",money*0.92)
        tien=money*0.92
        print("tiền taxi là:",tien)
    else:
        print("tiền taxi là:",money)
else:
    print("không xác định được")
