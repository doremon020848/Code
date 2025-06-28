#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW01_4
# 229223 Sec 001

a = int(input("x:"))
b = int(input("y:"))
n = (a-1)

s_m = int(((b*(b+1)) / 2 ) -  (((n*(n+1)) / 2 )))    # ใช้สูตร (n(n+1)) / 2
                                                     # ถ้าค่าเริ่มต้นไม่ใช่ 1 ให้ ใช้สูตร (n(n+1)) / 2 - (l(nl+1)) / 2  โดยกำหนดให้  l = n-1  

print("Answer",s_m)

