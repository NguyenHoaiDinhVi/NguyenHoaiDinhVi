# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:14:23 2024

@author: nguyenhoaidinhvi
"""

print("3 cạnh a,b,c có tạo thành 3 cạnh của một tam giác")
a=float(input("nhập cạnh a:"))
b=float(input("nhập cạnh b:"))
c=float(input("nhập cạnh c:"))
if a+b>c or a+c>b or b+c>a:
    if a==b or a==c or b==c:
        print("tam giác là tam giác cân")
    elif a==b==c:
        print("tam giác là tam giác đều")
    elif (a**2==b**2+c**2 ) or (b**2==a**2+c**2) or (c**2==a**2+b**2):
        print("tam giác là tam giác vuông")
    else:
        print("tam giác là tam giác thường")