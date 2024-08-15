# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:26:42 2024

@author: Nguyenhoaidinhvi
"""
print("kiểm tra thử 3 cạnh a,b,c có phải là 3 cạnh của một tam giác không?")
a=float(input("nhập cạnh a(cm):"))
b=float(input("nhập cạnh b(cm):"))
c=float(input("nhập cạnh c(cm):"))
if a+b>c or a+c>b or b+c>a:
    print("a,b,c là ba cạnh của một tam giác")
else:
    print("a,b,c không phải là ba cạnh của một tam giác")