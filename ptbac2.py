# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:40:13 2024

@author: nguyenhoaidinhvi
"""
print("giải phương trình bậc hai a*x**2 +bx+c=0")
a=float(input("nhập giá trị của a:"))
b=float(input("nhập giá trị của b:"))
c=float(input("nhập giá trị của c:"))
delta= b**2- (4*a*c)
if delta<0:
    print("phương trình vô nghiệm")
elif delta==0:
    print("phương trình có một nghiệm kép")
    print("x1=x2=",-b/2*a)
elif delta>0:
    print("phương trình có 2 nghiệm")
    import math
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a))
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a))
else:
    print("không xác định được")
    