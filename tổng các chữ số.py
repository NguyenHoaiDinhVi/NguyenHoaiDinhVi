# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:46:55 2024

@author: Student
"""

print("nhập 1 số nguyên dương có 2 chữ số")
a=int(input("a="))
if a<=99 and a>=1:
    x=a%10
    y=a//10
    b=x+y
    print("tổng các chữ số=",b)
else:
    print("không xác định")    
    