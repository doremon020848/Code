#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab02_2
# 229223 Sec 001

def main():
    a = int(input("จงส่งค่าที่เจ้าอยากรู้มา:"))
    reverse_digits(a)
    b = reverse_digits(a)
    print( "เอาคำตอบไปเลยจ้า:", b)


# implement ฟังก์ชันนี้ให้ถูกต้อง
# ทำให้ฟังชั่นรู้หลักตัวเอง
def reverse_digits(a):
    s1 = (a // 1000)
    s2 = (a%1000) // 100
    s3 = (a%100) // 10
    s4 = (a%10)
#  นำค่ามาเรียงกลับกัน
    c1 = s4 * 1000
    c2 = s3 * 100
    c3 = s2 * 10
    c4 = s1
    mana = (c1 + c2 + c3 +c4)
    return mana


if __name__ == '__main__':
    main()
