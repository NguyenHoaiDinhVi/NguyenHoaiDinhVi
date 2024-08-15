# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:19:58 2024

@author: nguyenhoaidinhvi
"""
GPA=float(input("nhập điểm của bạn:"))
if GPA <3.5:
    print("học lực kém")
elif 3.5<= GPA  <5.0:
    print("học lực yếu")
elif 5.0<= GPA  <7.0:
    print("học lực trung bình")
elif 7.0<= GPA  <8.0:
    print("học lực khá")
elif 8.0<= GPA  <9.0:
    print("học lực giỏi")
elif 9.0<= GPA  <10:
    print("học lực xuất sắc")
else:
    print("không xác định được")