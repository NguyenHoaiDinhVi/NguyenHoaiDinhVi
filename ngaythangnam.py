# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:55:51 2024

@author: Student
"""
print("kiểm tra tính hợp lệ của ngày tháng năm")
y=float(input("nhập năm:"))
if 0<y<2025:
    if (y%4==0 and y%100==0) or y%400==0:
        m=float(input("nhập tháng:"))
        if 1<=m<=12:
            if m==2:
                d=float(input("nhập ngày:"))
                if 1<=d<=29:
                    print("hợp lệ")
                else:
                    print("không hợp lệ")
            if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
                d=float(input("nhập ngày:"))
                if 1<= d<= 31:
                    print("hợp lệ")
                else:
                    print("không hợp lệ")
            if m==4 or m==6 or m==9 or m==11:
                d=float(input("nhập ngày:"))
                if 1<=d<=30:
                    print("hợp lệ")
                else:
                    print("không hợp lệ")
    else:
        m=float(input("nhập tháng"))
        if 1<=m<=12:
            if m==2:
                d=float(input("nhập ngày:"))
                if 1<=d<=28:
                    print("hợp lệ")
                else:
                    print("không hợp lệ")
            if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
                d=float(input("nhập ngày:"))
                if 1<= d<= 31:
                    print("hợp lệ")
                else:
                    print("không hợp lệ")
            if m==4 or m==6 or m==9 or m==11:
                d=float(input("nhập ngày:"))
                if 1<=d<=30:
                    print("hợp lệ")
                else:
                    print("không hợp lệ")
                
                
              