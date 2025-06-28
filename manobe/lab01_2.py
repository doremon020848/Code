#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW01_2
# 229223 Sec 001


x = int(input("How many milliseconds do you need?: "))         # รับค่า input
d = int( x // ( (8.64)*(10)**7) )                              # ได้ค่า x มาเเล้วน้ำมาหา day
# print("day",d)

z = int( x % ( (8.64)*(10)**7) )                               # นำ input มาหาเศษเกินเพื่อนำไปหาค่าต่อ
h = int( z // ( (3.6)*(10)**6) )                               # ได้เศษเกินเเล้วนำมาหาค่า hour
# print("hour",h)

q = int( z % ( (3.6)*(10)**6) )                                # หาเศษเกิน
m = int( q // 60000)                                           # นำมาหาค่า minute
# print("minute",m)

p = int( q % 60000 )                                           # หาเศษเกิน
s = int( p // 1000)                                            # นำมาหาค่า second
# print("second",s)

i = int( p % 1000)                                             # หาเศษเกิน
mi =int( i )                                                   # นำมาหาค่า milliseconds
# print("milliseconds",mi)

print("day", d,"hour", h,"minute", m,"second", s,"milliseconds",mi)
