#!/usr/bin/env python3
# thanathorn chanaphochai benz
# 670510755
# HW02_2
# 229223 Sec 001
# กำหนด input รับค่า
def main():
    number = int(input())
    k = int(input())
    kth_digit(number,k)
    test_kth_digit()
# ตั้งสมาการ
def kth_digit(number, k):
    x = (abs(number) //  (10 ** k)) % 10
    return x
# teat 
def test_kth_digit():
    assert kth_digit(789, 0) == 9
    assert kth_digit(789, 1) == 8
    assert kth_digit(-789, 2) == 7
    print( "All ok")



if __name__ == '__main__':
    main()
