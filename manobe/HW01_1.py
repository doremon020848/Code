#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW01_1
# 229223 Sec 001

#รับค่าเข้ามา
a = float(input("m1:"))
b = float(input("b1:"))
c = float(input("m2:"))
d = float(input("b2:"))
#ใช้สูตรที่ให้มา
x = (d-b) / (a-c)       
f = (a*x)+b

#print ให้ออกมาเป็น ทศนิยมสองตำเเหน่ง ด้วยใช้ (%.2f,%.2f) เเละ ทำให้เป็นคู่อันดับ
print("Lines intersect at (%.3f,%.3f)" % (x,f))